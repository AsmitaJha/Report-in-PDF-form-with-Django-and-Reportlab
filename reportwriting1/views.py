from django.shortcuts import render
from rest_framework import viewsets
from .models import Report,Methodology
from .serializers import ReportSerializer,MethodologySerializer
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from django.http import HttpResponse

# Create your views here.
class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    
class MethodologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Methodology.objects.all()
    serializer_class=MethodologySerializer
    
from django.shortcuts import render
from rest_framework import viewsets
from .models import Report,Methodology
from .serializers import ReportSerializer,MethodologySerializer
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from django.http import HttpResponse

# Create your views here.
class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    
class MethodologyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Methodology.objects.all()
    serializer_class=MethodologySerializer
    
'''def generate_pdf(request):
    
    buffer=BytesIO()
    p=canvas.Canvas(buffer,pagesize=A4)
    
    width,height=A4
    
    y=height-50
    x=20
    
    report=Report.objects.all()
    
    p.drawString(100, height-100, "Test PDF Content")
    def separator_line():
        nonlocal y
        p.line(40,y,width-10,y)
        y-=20
     
    def extract_contents(contents, font="Helvetica", size=12,bold=False,alignment=1):
        nonlocal y  # Assuming y_pos is defined outside this function
        
        # Define paragraph style
        style = ParagraphStyle(name='Normal',
                            fontName=font,
                            fontSize=size,
                            leading=size + 4,rightIndent=120,justifyBreaks=180)  # Adjust leading as needed
        
        # Create a Paragraph object with the specified style
        para = Paragraph(contents, style)
        
        # Draw the Paragraph on the canvas
        para.wrapOn(p, 400, 40)  # Adjust width and height as needed
        para.drawOn(p, 50, y-20)

        # Update y for the next text placement
        y -= para.height-20
        
    p.setFont("Times-Bold", 20)

    for instance in report:
        p.drawString(200, y, instance.intial_line)
        y-=50
        
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    return response'''
    
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4

def generate_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    report=Report.objects.all()
    methodology=Methodology.objects.all()
    width, height = A4
    p.setFont("Times-Bold", 20)
    custom_style=ParagraphStyle(name='CustomStyle',fontName='Times-Roman',fontSize=12) 
    
        #p.drawString(40,height-15,instance.introduction)
    def check_page_break(p, y, height, threshold=50):
        if y < threshold:
            p.showPage()
            p.setFont("Times-Roman", 12)
            return height - 50
        return y
    '''def extract_contents(contents, font="Helvetica", size=12,bold=False,alignment=1):
        nonlocal height # Assuming y_pos is defined outside this function
        
        # Define paragraph style
        style = ParagraphStyle(name='Normal',
                            fontName=font,
                            fontSize=size,
                            leading=size + 4,rightIndent=-164,justifyBreaks=180)  # Adjust leading as needed
        
        # Create a Paragraph object with the specified style
        para = Paragraph(contents, style)
        
        # Draw the Paragraph on the canvas
        para.wrapOn(p, 400, 40)  # Adjust width and height as needed
        para.drawOn(p, 50, height-185)
    
    # Update y_pos for the next text placement
        height -= para.height-20'''
    my_Style=ParagraphStyle("Own Style",rightIndent=-164,fontName='Times-Roman')
    styles = getSampleStyleSheet()
    y=height - 50
     
    for instance in report:
        p.drawString(240,y,instance.intial_line)
        y-=50
        y=check_page_break(p,y,height)
        p.drawString(164,y,instance.title)
        y-=20
        y=check_page_break(p,y,height)
        #For Objective
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Objective:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p1=Paragraph(instance.objective,styles["Normal"])
        p1.wrapOn(p,550,50)
        p1.drawOn(p,40,y-p1.height)
        y -= p1.height + 20
        y = check_page_break(p, y, height)
        
        #For Introduction
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Motivation:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p2=Paragraph(instance.motivation,styles['Normal'])
        p2.wrapOn(p,550,50)
        p2.drawOn(p,40,y-p2.height)
        y-=p2.height + 20
        y = check_page_break(p, y, height)
        #For Methodology
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Introduction:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p3=Paragraph(instance.introduction,styles['Normal'])
        p3.wrapOn(p,550,50)
        p3.drawOn(p,40,y-p3.height)
        #p.drawString(40,height-15,instance.introduction)
        #Overview
        height-=p3.height+45
        y -= p3.height + 20
        y = check_page_break(p, y, height)
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Overview of the Project:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p4=Paragraph(instance.project_overview,styles['Normal'])
        p4.wrapOn(p,550,50)
        p4.drawOn(p,40,y-p4.height)
        y -= p4.height + 20
        y = check_page_break(p, y, height)
        
        #Methodology
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Methodology:")
        y -= 15
        y = check_page_break(p, y, height)
        
        
        for instance1 in methodology:
            
            #Library Import
            p.drawString(35, y, "\u2022")
            p.setFont("Times-Bold",12)
            p.drawString(45,y,"Importing Necessary Libraries:")
            y -= 5
            y = check_page_break(p, y, height)
            p.setFont("Times-Roman",12)
            #height-=5
            p5=Paragraph(instance1.libray_module_import,styles['Normal'])
            p5.wrapOn(p,550,50)
            p5.drawOn(p,40,y-p5.height)
            y -= p5.height + 20
            y = check_page_break(p, y, height)
  
            # Dropping Unnecessary Columns
            p.drawString(35, y, "\u2022")
            p.setFont("Times-Bold",12)
            p.drawString(45,y,"Droppin Unnecessary Columns:")
            y -= 5
            y = check_page_break(p, y, height)
            p.setFont("Times-Roman",12)
            
            p6=Paragraph(instance1.column_drop,styles['Normal'])
            p6.wrapOn(p,550,50)
            p6.drawOn(p,40,y-p6.height)
            y -= p6.height + 20
            y = check_page_break(p, y, height)
            
            
            # Data Preprocessing
            p.drawString(35, y, "\u2022")
            p.setFont("Times-Bold",12)
            p.drawString(45,y,"Data Preprocessing:")
            y -= 5
            y = check_page_break(p, y, height)
            p.setFont("Times-Roman",12)
            
            p7=Paragraph(instance1.preprocessing)
            p7.wrapOn(p,550,50)
            p7.drawOn(p,40,y-p7.height)
            y -= p7.height + 20
            y = check_page_break(p, y, height)
            # Stemming
            p.drawString(35, y, "\u2022")
            p.setFont("Times-Bold",12)
            p.drawString(45,y,"Stemming and Polarity Determination:")
            y -= 5
            y = check_page_break(p, y, height)
            p.setFont("Times-Roman",12)
            p8=Paragraph(instance1.stemming,styles['Normal'])
            p8.wrapOn(p,550,50)
            p8.drawOn(p,40,y-p8.height)
            y -= p8.height + 20
            y = check_page_break(p, y, height)
            
            
        # Discussion
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Discussion:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p9=Paragraph(instance.discussion,styles['Normal'])
        p9.wrapOn(p,550,50)
        p9.drawOn(p,40,y-p9.height)
        y -= p9.height + 20
        y = check_page_break(p, y, height)
        
        # Conclusion
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Conclusion:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p10=Paragraph(instance.conclusion,styles['Normal'])
        p10.wrapOn(p,550,50)
        p10.drawOn(p,40,y-p10.height)
        y -= p10.height + 20
        y = check_page_break(p, y, height)
        
        #Reference
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Reference:")
        y -= 5
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p11=Paragraph(instance.references,styles['Normal'])
        p11.wrapOn(p,550,50)
        p11.drawOn(p,40,y-p11.height)
        y -= p11.height + 20
        y = check_page_break(p, y, height)
        # Project Link
        p.setFont("Times-Bold",12)
        p.drawString(30,y,"Project Link:")
        y -= 15
        y = check_page_break(p, y, height)
        p.setFont("Times-Roman",12)
        p.drawString(40,y,instance.project_links)
        y -= 20
        y = check_page_break(p, y, height)
        
    p.showPage()
    
    p.save()
    
    pdf = buffer.getvalue()
    buffer.close()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'
    return response

        
        
        
        
        
        
    
    
    
    

        
        
        
        
        
        
    
    
    
    