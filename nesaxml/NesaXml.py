from past.builtins import basestring

from re import sub
from decimal import Decimal
from datetime import datetime

from enum import Enum

DATETIME_FORMAT = r"%Y-%m-%dT%H:%M:%S"

class FieldType(Enum):
    string   = "xs:string"
    integer  = "xs:integer"
    money    = "xs:decimal"
    decimal  = "xs:decimal"
    datetime = "xs:dateTime"

class NesaXml(object):
    def __init__(self, data=None):
        if data is not None:
            for element in self._defn:
                name = element["name"]
                if name in data:
                    self._validate(element, data[name])

            self._data = data
        else:
            self._data = {}

    def _validate(self, element, value):
        if element["type"] is FieldType.string:
            length = element.get("length", None)
            if not isinstance(value, basestring):
                raise ValueError("Value is not of type %s" % element["type"])
            if length is not None and len(value) > length:
                raise ValueError("Value is too long. Max: %s" % length)
            if length is not None and len(value) == 0 and element.get("mandatory", False):
                raise ValueError("Value is required (string of length 0)")
        elif element["type"] is FieldType.integer:
            if not isinstance(value, int):
                raise ValueError("Value is not an integer")
        elif element["type"] is FieldType.money:
            if not isinstance(value, float) and not isinstance(value, Decimal):
                if isinstance(value, basestring):
                    value = Decimal(sub(r'[^\d\-.]', '', value))
                else:
                    raise ValueError("Unable to parse a money value")
        elif element["type"] is FieldType.datetime:
            if not isinstance(value, datetime):
                if isinstance(value, basestring):
                    value = datetime.strptime(value, DATETIME_FORMAT)
                else:
                    raise ValueError("Unable to parse a datetime value")
    
    def __getattr__(self, name):
        if name.startswith('_'):
            return super(NesaXml, self).__getattr__(name)
        
        element = None
        for elt in self._defn:
            if elt["name"] == name:
                element = elt
                break
        
        if element is None:
            raise AttributeError
        else:
            return self._data.get(name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super(NesaXml, self).__setattr__(name, value)
        
        element = None
        for elt in self._defn:
            if elt["name"] == name:
                element = elt
                break
        
        if element is None:
            raise AttributeError
        else:
            self._validate(element, value)
            self._data[name] = value

    def __repr__(self):
        elts = []

        for element in self._defn:
            name = element["name"]
            type_label = element["type"].name
            length_label = element.get("length", None)

            if length_label is None:
                label = ' %s (%s)' % (name, type_label)
            else:
                label = ' %s (%s: %s)' % (name, type_label, str(length_label))

            if name in self._data:
                elts.append(label + ': %s' % self._data[name])
            elif element.get("mandatory", False):
                elts.append(label + ': <Requires Value>')
            else:
                elts.append(label + ': <No Value>')
            
        elt_str = '\n'.join(elts)
        return ('<%s\n' % self.__class__.__name__) + elt_str + ('\n>')

    def _to_xml_value(self, defn_type, value):
        if defn_type is FieldType.datetime:
            return datetime.strftime(DATETIME_FORMAT)
        else:
            return str(value)

    def _generate_elements(self, doc, tag, text):
        for elt in self._defn:
            name = elt["name"]
            if name not in self._data:
                if elt.get("mandatory", False):
                    raise ValueError("%s is a mandatory field" % name)
                else:
                    pass # skip this field
            else:
                min_occurs = 1 if elt.get("mandatory", False) else 0
                with tag(
                    'xs:element',
                    name=name,
                    type=elt["type"].value,
                    minOccurs=min_occurs
                ):
                    text(self._to_xml_value(elt["type"], self._data[name]))


    def to_xml_doc(self):
        from yattag import Doc

        doc, tag, text = Doc().tagtext()

        with tag('xs:element', name=self._name):
            with tag('xs:complexType'):
                with tag('xs:sequence'):
                    self._generate_elements(doc, tag, text)
        
        return doc

    def to_xml_string(self, indent=False):
        from yattag import indent

        result = self.to_xml_doc().getvalue()

        if indent:
            return indent(result)
        else:
            return result

def createXmlClass(name, defn):
    return type(name, (NesaXml,), {
        "_name": name,
        "_defn": defn
    })
