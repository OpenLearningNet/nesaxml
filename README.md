# NESA XML for Bulk Upload

Python library for generating XML according to the NESA Schema for Bulk Upload.

## Dependenices
- future (if using python 2.7)
- yattag

## Classes

The NesaXML class is the base class for all XML elements. This library defines subclasses for each element, implemented according to the provided XML Schema. e.g.


   from nesaxml import Course


NesaXML subclasses defined for the following elements:
- Course
- CourseSession
- CourseLocation
- CourseStandard
- CourseSyllabus
- CourseProvider
- ProviderLocation
- CourseParticipation
- CourseParticipation

Each of these may be constructed using an optional data dict, e.g.

    from nesaxml import CourseLocation

    course_loc = CourseLocation()

    # or

    # validate initial data
    course_loc2 = CourseLocation({
        "obs_Course_code": "ABC123"
    })


Each implements validated setters, and getters for each property, e.g.

    code = course_loc.obs_Course_code
    course_loc.obs_Course_code = code

And each has an XML generation method:

    # this will fail if mandatory fields have not been provided
    xml_string = course_loc.to_xml_string(indent=True)

N.B. __repr__ is defined for these classes, e.g.

    >>> course_loc
    <CourseLocation
     obs_Course_code (string: 20): ABC123
     obs_ProviderLocation_code (string: 20): <Requires Value>
    >
