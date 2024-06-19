#!/usr/bin/env python
# coding: utf-8

# In[1]:


def savings(gross_pay, tax_rate, expenses):   
    gross_pay = int(gross_pay)
    tax_rate = float(tax_rate)
    expenses = int(expenses)   
    
    if 0 < tax_rate < 1:  
        tax = gross_pay * tax_rate
        takeHome_pay = gross_pay - tax - expenses
        return int(takeHome_pay)
    else:
        return None


# In[3]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material = int(total_material)
    material_units = str(material_units)
    num_jobs = int(num_jobs)
    job_consumption = int(job_consumption)
    
    consumed_material = num_jobs * job_consumption
    remaining_material = total_material - consumed_material 
    remaining_material = max(remaining_material, 0)

    return str(remaining_material) + material_units


# In[5]:


def interest(principal, rate, periods):
    principal = int(principal)
    rate = float(rate)
    periods = int(periods)
    
    final_value = int(principal * (rate * periods) + principal)

    return final_value

