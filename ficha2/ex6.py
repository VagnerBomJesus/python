

c1 = 1500*((1+0.02)**1)
c2 = 1500*((1+0.025)**1)
c3 = 1500*((1+0.03)**1)

c12 = 1500*((1+0.02)**2)
c22= 1500*((1+0.025)**2)
c32 = 1500*((1+0.03)**2)

c13 = 1500*((1+0.02)**3)
c23 = 1500*((1+0.025)**3)
c33 = 1500*((1+0.03)**3)

print(f'1500 $     2.0%    2.5%    3.0%')
print(f'2023       {c1:.2f}     {c2:.2f}    {c3:.2f} ')
print(f'2024       {c12:.2f}     {c22:.2f}    {c32:.2f}')
print(f'2025       {c13:.2f}     {c23:.2f}    {c33:.2f}')
