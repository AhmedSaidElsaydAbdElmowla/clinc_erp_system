from odoo import models, fields ,api

class ClincPatients(models.Model):
    
    _name = 'clinc.patients'  #this is a new object from class and we name it (and use it in form view)
    _description = 'all data you want add it here about object'
    
    #in new object we creat four fields to user to put hes name 
    
    first_name = fields.Char(string= 'first name ', required=True)
    second_name = fields.Char(string= 'first name ', required=True)
    third_name = fields.Char(string= 'first name ', required=True)
    forth_name = fields.Char(string= 'first name ', required=True)
    
    #type in this fields is char
    #attributs in this field is string  and required
    
    name = fields.Char(string="Name", readonly=True, compute='get_patient_name') #the compute take his vale from function 
    image = fields.Binary(string='Image', copy=False)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender',default='male')
    birth_day = fields.Date(string='Birthday', required=True)
    met_doctor = fields.Boolean(string='Met Doctor')
    last_meeting = fields.Date(string='Last Meeting')




    @api.one
    def get_patient_name(self):
        
        #function to calculate the full name for the patient
        
        self.name = self.first_name+' '+self.second_name+' '+self.third_name+' '+self.forth_name



#int age of he user
age_year = fields.Integer(string="Years", compute='calculate_age')
age_month = fields.Integer(string="Months", compute='calculate_age')
age_day = fields.Integer(string="Days", compute='calculate_age')

#function to calcolate the age of he user

@api.one
def calculate_age(self):


    if self.birth_day :
        birth_day = str(self.birth_day)
        current_date = str(fields.Date.today())


    birth_day_year_as_int = int(birth_day[0]+birth_day[1]+birth_day[2]+birth_day[3])
    birth_day_month_as_int = int(birth_day[5]+birth_day[6])
    birth_day_day_as_int = int(birth_day[8]+birth_day[9])




    current_date_year_as_int = int(current_date[0]+current_date[1]+current_date[2]+current_date[3])
    current_date_month_as_int = int(current_date[5]+current_date[6])
    current_date_day_as_int = int(current_date[8]+current_date[9])


    period_years = current_date_year_as_int-birth_day_year_as_int
    period_months = current_date_month_as_int-birth_day_month_as_int
    period_days = current_date_day_as_int-birth_day_day_as_int


    months_list_1 = ['04','06','09','11']
    months_list_2 = ['01','03','05','07','08','10','12']


    if period_days < 0:
      if str(current_date_month_as_int) == '02':
        if current_date_year_as_int%4 == 0:
           period_days = 29+period_days
    
    if current_date_year_as_int%4 != 0:
       period_days = 28+period_days
       
       
    for index in range(0,4):
        if current_date_month_as_int == int(months_list_1[index]):
           period_days = 30+period_days
        
        
    for index in range(0,7):
        if current_date_month_as_int == int(months_list_2 [index]):
           period_days = 31+period_days
           period_months = period_months-1
            
        if period_months < 0:
           period_months = 12+period_months
           period_years = period_years-1


        self.age_year = period_years
        self.age_month = period_months
        self.age_day = period_days


    