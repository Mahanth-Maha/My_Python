print("--------------EMAIL SLICER --------------")
z='y'
while(z=='y' or z=='Y' ):
    x=input("Enter the Email : ")
    domain=[]
    user=[]
    dom_name=[]
    dom_type=[]
    r_domain = r_user = r_dom_name = r_dom_type=''
    
    #Email  ==> mahanth@gmail.com
    email=list(x)
    for i in range(len(email)):
        if(email[i]=='@'):
            c=i
        if(email[i]=='.'):
            d=i
    #User Name ==> mahanth
    for i in range(c):
        user.append(email[i])
    #Domain ==> gmail.com
    for i in range(c+1,len(email)):
        domain.append(email[i])
    #Domain Name ==> gmail
    for i in range(c+1,d):
        dom_name.append(email[i])
    #Domian Type ==> com
    for i in range(d+1,len(email)):
        dom_type.append(email[i])
    
    for i in user:
        r_user += i
    for i in dom_name:
        r_dom_name += i
    for i in dom_type:
        r_dom_type += i
    for i in domain:
        r_domain += i
    
    print("EMAIL",x,'SLICECED\n')
    print("USER ID\t\t:",r_user)
    print("Domian Name\t:",r_dom_name)
    print("Type\t\t:",r_dom_type)
    print("DOMAIN\t\t:",r_domain) 

    z=input("\npress y to add another email :")
