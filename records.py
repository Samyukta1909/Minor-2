import dns.resolver
recordList=[]
recordList1=[] 
def record(domainname):
    try:
        dns.resolver.resolve(domainname, 'NS')
        # recordList.append("A Records:")
        try:
            a_name=dns.resolver.resolve(domainname,'A')
            for rec in a_name:
                a=rec.to_text()
                recordList.append(a)
        # except dns.resolver.NoAnswer:
        except Exception as e:
            pass
            print("Exception in: ",e)
            m="No record found"
            recordList.append(m)
         
        # recordList1=[]       
        # recordList1.append("CNAME Records;")    
        try:
            c_name=dns.resolver.resolve(domainname,'CNAME')
            for recd in c_name:
                c=recd.to_text()
                recordList1.append(c)
        except dns.resolver.NoAnswer:
            pass
            d="No record found"
            recordList1.append(d)
    
    except dns.resolver.NXDOMAIN:
        d="UNREGISTERED URL"
        recordList.append(d)
        recordList1.append(d)
    
    return recordList,recordList1