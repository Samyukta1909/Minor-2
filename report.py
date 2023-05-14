from fpdf import FPDF
import time
from records import recordList,recordList1
from domain import domainList
from subdomains import subdomainList
from endpoints import endpointsList
from sensitiveFiles import hidFilesList


def header(self):
    # Logo
    self.image('static/images/logo.png', 10, 8, 33)
    # Arial bold 15
    self.set_font('Arial', 'B', 15)
    # Move to the right
    
    # Title
    self.ln(4)
    self.cell(33)
    self.cell(0, 10, 'Eagle Eye Report', 1, 2, 'C')
    # Line break
    self.ln(2)

def targetname(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, subdomainList[0], 0, 0, 'C')
    self.ln(18)

  
def arecord(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, 'A Records', 0, 0, 'C')
    self.ln(10)

def crecord(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, 'C Name Records', 0, 0, 'C')
    self.ln(10)

def whoisinfo(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, 'WHOIS Information', 0, 0, 'C')
    self.ln(10)

def subdomaintitle(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, 'Subdomains', 0, 0, 'C')
    self.ln(10)

def endpointtitle(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, 'Endpoints', 0, 0, 'C')
    self.ln(10)

def sensitivetitle(self):
    self.set_font('Arial', 'B', 13)
    self.cell(2)
    self.cell(0, 10, 'Sensitive Files', 0, 0, 'C')
    self.ln(10)

def createreport():
    print("record list: ",recordList)
    fpdf = FPDF()
    
    fpdf=FPDF('P','mm','Letter')
    
    fpdf.add_page()
    header(fpdf)
    
    fpdf.set_font('times','',12)
    
    fpdf.ln(15)
    targetname(fpdf)
    fpdf.set_font('times','',12)
   
   
    
    arecord(fpdf)
    fpdf.set_font('times','',12)
    
    fpdf.set_font('times','',12)
    for i in range(len(recordList)):
       
        fpdf.cell(0,10,recordList[i], ln=True)
        
      
    crecord(fpdf)
    fpdf.set_font('times','',12)
   
   
    for i in range(len(recordList1)):
       
        fpdf.cell(0,10,recordList1[i], ln=True)
    
    whoisinfo(fpdf)
    fpdf.set_font('times','',12)
 
   
    for i in range(len(domainList)):
        fpdf.multi_cell(0,10,domainList[i])

    subdomaintitle(fpdf)
    fpdf.set_font('times','',12)
    
    
    for i in range(1,len(subdomainList)):
        fpdf.cell(0,10,subdomainList[i], ln=True)

    endpointtitle(fpdf)
    fpdf.set_font('times','',12)
   
   
    
    for i in range(len(endpointsList)):
        fpdf.cell(0,10,endpointsList[i], ln=True)

    sensitivetitle(fpdf)
    fpdf.set_font('times','',12)
    
    
    for i in range(len(hidFilesList)):
        fpdf.multi_cell(0,10,hidFilesList[i])

    
    fpdf.set_font('times','',12)
    fpdf.output('myreport/EagleEyeReport.pdf')
    time.sleep(2)

