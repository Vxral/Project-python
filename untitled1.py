import tkinter
​import​ ​json 
  def​ ​submit​(): 
 ​    ​l3​.​configure​(​text​=​"Start"​) 
 ​    ​f​ ​=​ ​open​(​"jim.json"​) 
 ​    lst ​=​ ​json​.​load​(​f​) 
 ​    ​user​ ​=​ ​e1​.​get​() 
 ​    ​alamat​=​[​"!"​,​"@"​,​"$"​,​"%"​,​"*"​,​"_"​,​" "​,​"."​,​","​,​"~"​,​"#"​,​"&"​,​"("​,​")"​,​"^"​,​"/"​,​"'"​,​'"'​,​"+"​,​"-"​,​"|"​] 
 ​    ​if​ ​user​ ​in​ lst: 
 ​        ​l3​.​configure​(​text​="Already Taken"​) 
 ​    ​else​: 
 ​         for​ ​i​ ​in​ ​user​: 
 ​             ​if​ ​i​ ​in​ ​alamat​: 
 ​                    ​l3​.​configure​(​text​=​"Just Number And Alamat"​) 
 ​               ​else​: 
 ​                    ​l3​.​configure​(​text​=​"Done!"​) 
 ​                    ​newuser​=​{​e1​.​get​():​e2​.​get​()} 
 ​                     
 ​                    ​with​ ​open​(​'jim.json'​) ​as​ ​file​: 
 ​                        ​data​=​json​.​load​(​file​) 
 ​                    ​with​ ​open​(​'jim.json'​,​'w'​) ​as​ ​file​: 
 ​                        ​data​.​update​(​newuser​) 
 ​                        ​file​.​seek​(​0​) 
 ​                        ​json​.​dump​(​data​,​file​) 
 ​             
 ​def​ ​login​(): 
 ​    ​username​=​e1​.​get​() 
 ​    ​password​=​e2​.​get​() 
 ​    ​f​ ​=​ ​open​(​"jim.json"​) 
 ​    ​lst​ ​=​ ​json​.​load​(​f​) 
 ​    ​if​ ​username​ ​in​ lst: 
 ​        ​if​ ​lst[​username​]​==​password​: 
 ​            ​l3​.​configure​(​text​=​"welcome"​) 
 ​        ​else​: 
 ​            ​l3​.​configure​(​text​=​"error"​) 
 ​    ​else​: 
 ​        ​l3​.​configure​(​text​=​"First SubMit"​) 
 ​     
  
 ​root​ ​= ​tkinter​.​Tk​() 
 ​root​.​geometry​(​"400x100"​) 
  
 ​l1 ​= ​tkinter​.​Label​(​root​,​text​=​"username:"​) 
 ​l2​ =​ tkinter​.​Label​(​root​,​text​=​"password:"​) 
 ​e1​ = ​tkinter​.​Entry​(​root​) 
 ​e2 ​= ​tkinter​.​Entry​(​root​) 
 ​l3​ =​ tkinter​.​Label​(​root​,​text​=​""​) 
 ​b1​ ​= ​tkinter​.​Button​(​root​,​text​=​"Submit"​,​command​=​submit​) 
 ​b2​ ​=​ tkinter​.​Button​(​root​,​text​=​"login"​,​command​=​login​) 
 
 ​l1​.​grid​(​row​=​0​,​column​=​0​) 
 ​l2​.​grid​(​row​=​0​,​column​=​1​) 
 ​e1​.​grid​(​row​=​1​,​column​=​0​) 
 ​e2​.​grid​(​row​=​1​,​column​=​1​) 
 ​l3​.​grid​(​row​=​1​,​column​=​2​) 
 ​b1​.​grid​(​row​=​2​,​column​=​0​) 
 ​b2​.​grid​(​row​=​2​,​column​=​1​) 
  
 ​root​.​mainloop​()