import whois

def WHOis(domain_name):
        d=whois.whois(domain_name)
        if (bool(d.domain_name)):
            domainList =[]
            whois_info =whois.whois(domain_name)
            dr = "Registrar: "+ str(whois_info.registrar)
            ur = "URL: "+ str(whois_info.registrar_url)
            cd = "Creation Date: "+ str(whois_info.creation_date)
            ed = "Expiration Date: "+ str(whois_info.expiration_date)
            ud = "Updated Date: "+ str(whois_info.updated_date)
            em = "Registrant Email: "+ str(whois_info.emails)
            st = "Status: "+ str(whois_info.status)
            domainList.append(dr)
            domainList.append(ur)
            domainList.append(cd)
            domainList.append(ed)
            domainList.append(ud)
            domainList.append(em)
            domainList.append(st)
            
            return domainList
        else:
            domainList =[]
            d="unregisterd url"
            domainList.append(d)
            return domainList 


