ages=[{
  'name':'hannah',
  'age':8
},
{
  'name':'betty',
  'age':7
},
{
  'name':'veronica',
  'age':5
},
{
  'name':'Austin',
  'age':15
}      
          ]

max_value=max(ages, key=lambda x:x['age'])
min_value=min(ages, key=lambda x:x['age'])
print(max_value)
print(min_value)