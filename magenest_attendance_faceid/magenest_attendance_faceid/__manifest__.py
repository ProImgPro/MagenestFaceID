{
    "name": "Hr Attendance FaceID",
    "summary": """
                Allows everyone to attendance using Webcam
                Develop by Magenest JSC """,
    "version": "0.1",
    "category": "Extra Tools",
    "website": "http://www.magenest.com",
    "author": "Magenest",
    "license": "OPL-1",
    "data": [
        "security/ir.model.access.csv",
        "security/faceid_manager.xml",
        "views/assets.xml",
        "views/faceid_hr_attendance_view.xml",
        ],
    "depends": ["web", 'hr'],
    "qweb": ["static/src/xml/web_widget_image_webcam.xml"],
    'images': ['static/images/icon.png'],

}
