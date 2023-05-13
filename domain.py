import whois
domainList =[]
def WHOis(domain_name):
        d=whois.whois(domain_name)
        if (bool(d.domain_name)):
            global domainList
            whois_info =whois.whois(domain_name)
            dn = "Domain Name: "+ str(whois_info.domain_name)
            dr = "Registrar: "+ str(whois_info.registrar)
            org = "Organization: "+ str(whois_info.org)
            ur = "URL: "+ str(whois_info.registrar_url)
            cd = "Creation Date: "+ str(whois_info.creation_date)
            ed = "Expiration Date: "+ str(whois_info.expiration_date)
            ud = "Updated Date: "+ str(whois_info.updated_date)
            em = "Registrant Email: "+ str(whois_info.emails)
            ds = "dnssec: "+ str(whois_info.dnssec)
            ad = "Address: "+ str(whois_info.address)
            domainList.append(dn)
            domainList.append(dr)
            domainList.append(org)
            domainList.append(ur)
            domainList.append(cd)
            domainList.append(ed)
            domainList.append(ud)
            domainList.append(em)
            domainList.append(ds)
            domainList.append(ad)
            
            return domainList
        
        else:
            domainList =[]
            d="UNREGISTERED URL"
            domainList.append(d)
            return domainList 


