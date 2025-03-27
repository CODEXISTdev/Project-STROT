from basics import Basics
# from temp import Basics
import os

class generator:
    def __init__(self):
        self.base= Basics()
        self.base.add_page()
        self.base.first_img()


    def exec_summary(self, para1, bullet, para2):
        self.base.heading1("Executive Summary")
        self.base.line()
        self.base.body(para1)
        self.base.bullet_points(bullet)
        self.base.body(para2)


    def summary_result(self, para1,para2):
        self.base.heading1("Summary of Results")
        self.base.body(para1)
        self.base.body(para2)



    def project_scope(self, para1, num1,para2,num2):
        self.base.heading1("Project Scope")
        self.base.body(para1)
        self.base.numbering_points(num1)
        self.base.body(para2)
        self.base.numbering_points(num2)
        self.base.add_page()


    def tech_details(self, para1):
        self.base.heading1("Technial Details")
        self.base.line()
        self.base.body(para1)


    def time_line(self, para1):
        self.base.heading2("Timeline of Events")
        self.base.body(para1)
        # table are incomplete
        self.base.add_page()

    def forensic(self,para1,para2,para3,para4,para5,para6,para7,para8,para9,bullet1,para10,para11,bullet2,para12,bullet3,para13,bullet4,para14,para15,para16,para17):
        self.base.heading1("Forensic Analysis")
        self.base.line()
        self.base.heading2("Materials Reviewed")
        self.base.body(para1)
        self.base.heading2("How the Attack Operated")
        self.base.heading3("December Exploid")
        self.base.body(para2)
        # self.base.body(para2)
        # self.base.body(para2)
        # self.base.body(para2)
        self.base.body(para3)
        self.base.body(para4)
        self.base.body(para5)
        self.base.body(para6)
        self.base.add_page()
        self.base.heading3("January Exploit")
        self.base.body(para7)
        self.base.body(para8)
        self.base.heading3("Both Exploits")
        self.base.body(para9)
        self.base.bullet_points(bullet1)
        self.base.heading2("Indicators of Compromise")
        self.base.body(para10)
        self.base.heading3("December Exploit")
        self.base.body(para11)
        self.base.bullet_points(bullet2)
        self.base.body(para12)
        self.base.bullet_points(bullet3)
        self.base.heading3("January Exploit")
        self.base.body(para13)
        self.base.bullet_points(bullet4)
        self.base.body(para14)
        self.base.heading2("Validation of Accelion Remedition of the Exploied Valnebilities")
        self.base.body(para15)
        self.base.body(para16)

        self.base.body(para17)


    def table(self,column,data):
        self.base.add_table(column,data)


    def testing(self,para1,bullet,para2,para3,para4,para5,para6,para7,para8):
        self.base.heading2("Testing FTA for Additional Vulnerabilities")
        self.base.heading3("Objectives and Methodology")
        self.base.body(para1)
        self.base.bullet_points(bullet)
        self.base.body(para2)
        self.base.body(para3)
        self.base.body(para4)
        self.base.body(para5)
        self.base.heading3("Results of Testing FTA for Additional Vulnerabilities")
        self.base.body(para6)
        self.base.body(para7)
        self.base.body(para8)
        self.base.add_page()

    def desclaimer(self,disc):
        self.base.disclaimer(disc)


    def code_line(self, body_text):
        self.base.code(body_text)

    def savefile(self):
        self.base.save()

if __name__== "__main__":
    obj = generator()

    #executive summary
    obj.exec_summary("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",["ganesh", "pratik", "sidd","Vishnu"], """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.""")
    #
    # #Summary result
    obj.summary_result(""""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.""",)
    #
    #
    # #Project Scope
    obj.project_scope("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""",["ganesh", "pratik", "sidd"], """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.""",["ganesh", "pratik", "sidd"])

    #tech details
    obj.tech_details("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.""")

    #Timeline of Events
    obj.time_line("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.""")

    #forensic
    obj.forensic(""" Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a 
    galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
    Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
    It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
    ""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,
     but also the leap into electronic typesetting, remaining essentially unchanged. ""","""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
     scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. """,["Lorem Ipsum is simply dummy text of the printing and typesetting industry.","Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
    " when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries"," but also the leap into electronic typesetting, remaining essentially unchanged."],"""this the the bullet point in the project""","""who are we will take from NLP model","paste here and we will easly read it""",
                 ["this the the bullet point in the project","ganesh"],"""this also one of the paragraph""",["aurangya","khan","sheikh"],"""paragraph""",["first","second","third","fourth"],"""paragraph""","""paragraph""","""paragraph this is paragraph to check the""","""\n\n\n\nthis is the paragraph""")

    obj.table(["Id","name","age","city","Days"], [
        [1, "Alice", 24, "New York",11],
        [2, "Bob", 27, "Los Angeles",23],
        [3, "Charlie", 22, "Chicago",11],
        [4, "David", 30, "Houston",44],
        [5, "Eve", 28, "San Francisco",22]
    ])
    #Testing FTA for Additional Vulnerabilities
    obj.testing("""this is para""",["g","dfg","sdfg"],"""this is para""","""this is para""","""this is para""","""this is para""","""this is para""","""this is para""","""this is para""")

    #desclamer
    obj.desclaimer("""Disclaimer: While every precaution has been taken in the preparation of this document, neither Accellion norMandiant assumes any responsibility for errors or omissions resulting from the use of the information herein.""")
    obj.code_line("import os\nos.system('clear')\nfor i in range(10):\n\t\tprint(i)")
    # obj.code_line("hello")
    # obj.code_line("hello")



    #object save
    obj.savefile()

    #automatically open pdf
    os.system("open output.pdf")