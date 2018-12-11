from __future__ import absolute_import

from .NesaXml import createXmlClass, FieldType

Course = createXmlClass("Course", [
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_name",
        "type": FieldType.string,
        "length": 100,
        "mandatory": True
    },
    {
        "name": "obs_Course_duration",
        "type": FieldType.integer,
        "mandatory": True
    },
    {
        "name": "obs_Course_type",
        "type": FieldType.integer,
        "mandatory": True
    },
    {
        "name": "obs_URL",
        "type": FieldType.string,
        "length": 1000,
        "mandatory": False
    },
    {
        "name": "obs_ElementStandard",
        "type": FieldType.string,
        "length": 6000,
        "mandatory": True
    },
    {
        "name": "obs_ResearchMethodology",
        "type": FieldType.string,
        "mandatory": False
    },
    {
        "name": "obs_DeliveryStrategy",
        "type": FieldType.string,
        "mandatory": False
    },
    {
        "name": "obs_AssessmentStrategy",
        "type": FieldType.string,
        "mandatory": False
    },
    {
        "name": "obs_MaxParticipant",
        "type": FieldType.integer,
        "mandatory": False
    },
    {
        "name": "obs_Cost",
        "type": FieldType.money,
        "mandatory": False
    },
    {
        "name": "obs_SpecialRequirement",
        "type": FieldType.string,
        "mandatory": True
    },
    {
        "name": "obs_Recognition",
        "type": FieldType.string,
        "mandatory": False
    },
    {
        "name": "obs_EvaluationProcess",
        "type": FieldType.string,
        "mandatory": False
    },
    {
        "name": "obs_StudentStage",
        "type": FieldType.string,
        "length": 100,
        "mandatory": True
    },
    {
        "name": "obs_Status",
        "type": FieldType.integer,
        "mandatory": True
    },
    {
        "name": "obs_Description",
        "type": FieldType.string,
        "length": 2000,
        "mandatory": True
    },
    {
        "name": "obs_OnRequest",
        "type": FieldType.integer,
        "mandatory": False
    },
    {
        "name": "nsw_Jurisdiction",
        "type": FieldType.string,
        "length": 1,
        "mandatory": True
    }
])

CourseSession = createXmlClass("CourseSession", [
    {
        "name": "obs_Session_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_name",
        "type": FieldType.string,
        "length": 100,
        "mandatory": True
    },
    {
        "name": "obs_CommenceDate",
        "type": FieldType.datetime,
        "mandatory": True
    },
    {
        "name": "obs_EndDate",
        "type": FieldType.datetime,
        "mandatory": True
    },
    {
        "name": "obs_ProviderLocation_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": False
    }
])

CourseLocation = createXmlClass("CourseLocation", [
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_ProviderLocation_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    }
])

CourseStandard = createXmlClass("CourseStandard", [
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_Standard",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "nsw_Jurisdiction",
        "type": FieldType.string,
        "length": 1,
        "mandatory": True
    }
])

CourseSyllabus = createXmlClass("CourseSyllabus", [
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_name",
        "type": FieldType.string,
        "length": 100,
        "mandatory": True
    },
    {
        "name": "obs_StudentStage",
        "type": FieldType.string,
        "length": 100,
        "mandatory": True
    },
    {
        "name": "obs_LearningArea",
        "type": FieldType.string,
        "length": 300,
        "mandatory": True
    }
])

CourseProviderEvaluation = createXmlClass("CourseProviderEvaluation", [
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_Strengths",
        "type": FieldType.string,
        "mandatory": True
    },
    {
        "name": "obs_Challenges",
        "type": FieldType.string,
        "mandatory": True
    },
    {
        "name": "obs_Evaluation",
        "type": FieldType.string,
        "mandatory": False
    },
    {
        "name": "obs_Comments",
        "type": FieldType.string,
        "mandatory": False
    }
])

ProviderLocation = createXmlClass("ProviderLocation", [
    {
        "name": "obs_Location_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_name",
        "type": FieldType.string,
        "length": 250,
        "mandatory": True
    },
    {
        "name": "obs_addr",
        "type": FieldType.string,
        "length": 200,
        "mandatory": True
    },
    {
        "name": "obs_city",
        "type": FieldType.string,
        "length": 100,
        "mandatory": True
    },
    {
        "name": "obs_state",
        "type": FieldType.string,
        "length": 50,
        "mandatory": True
    },
    {
        "name": "obs_Postcode",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "nsw_GeoLoc",
        "type": FieldType.integer,
        "mandatory": False
    }
])

CourseParticipation = createXmlClass("CourseParticipation", [
    {
        "name": "obs_Course_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_Teacher_id",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    },
    {
        "name": "obs_Session_code",
        "type": FieldType.string,
        "length": 20,
        "mandatory": True
    }
])
