tmp1=open('submit_testv3_1.csv','r')
tmp2=open('submit_testv3_2.csv','r')
tmp3=open('submit_testv3_3.csv','r')
tmp4=open('submit_testv3_4.csv','r')
tmp5=open('submit_testv3_5.csv','r')
tmp6=open('submit_testv3_6.csv','r')
tmp7=open('submit_testv3_7.csv','r')
tmp8=open('submit_testv3_8.csv','r')
tmp9=open('submit_testv3_9.csv','r')
tmp10=open('submit_testv3_10.csv','r')
tmp11=open('../code/baseline.csv','r')
aa=open('submission_stacking_v4.csv','w+')
num=0
for q,w,e,r,t,y,u,i,o,p,z in zip(tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,tmp8,tmp9,tmp10,tmp11):
	num+=1
	if num==1:
		aa.write(q)
		aa.flush()
	else:
		p1=(float(q.strip().split(',')[1])+float(w.strip().split(',')[1])+float(e.strip().split(',')[1])+float(r.strip().split(',')[1])+float(t.strip().split(',')[1])+float(y.strip().split(',')[1])+float(u.strip().split(',')[1])+float(i.strip().split(',')[1])+float(o.strip().split(',')[1])+float(p.strip().split(',')[1]))/10
		p2=(float(q.strip().split(',')[2])+float(w.strip().split(',')[2])+float(e.strip().split(',')[2])+float(r.strip().split(',')[2])+float(t.strip().split(',')[2])+float(y.strip().split(',')[2])+float(u.strip().split(',')[2])+float(i.strip().split(',')[2])+float(o.strip().split(',')[2])+float(p.strip().split(',')[2]))/10
		p3=(float(q.strip().split(',')[3])+float(w.strip().split(',')[3])+float(e.strip().split(',')[3])+float(r.strip().split(',')[3])+float(t.strip().split(',')[3])+float(y.strip().split(',')[3])+float(u.strip().split(',')[3])+float(i.strip().split(',')[3])+float(o.strip().split(',')[3])+float(p.strip().split(',')[3]))/10
		p4=(float(q.strip().split(',')[4])+float(w.strip().split(',')[4])+float(e.strip().split(',')[4])+float(r.strip().split(',')[4])+float(t.strip().split(',')[4])+float(y.strip().split(',')[4])+float(u.strip().split(',')[4])+float(i.strip().split(',')[4])+float(o.strip().split(',')[4])+float(p.strip().split(',')[4]))/10
		p5=(float(q.strip().split(',')[5])+float(w.strip().split(',')[5])+float(e.strip().split(',')[5])+float(r.strip().split(',')[5])+float(t.strip().split(',')[5])+float(y.strip().split(',')[5])+float(u.strip().split(',')[5])+float(i.strip().split(',')[5])+float(o.strip().split(',')[5])+float(p.strip().split(',')[5]))/10
		p6=(float(q.strip().split(',')[6])+float(w.strip().split(',')[6])+float(e.strip().split(',')[6])+float(r.strip().split(',')[6])+float(t.strip().split(',')[6])+float(y.strip().split(',')[6])+float(u.strip().split(',')[6])+float(i.strip().split(',')[6])+float(o.strip().split(',')[6])+float(p.strip().split(',')[6]))/10
		p7=(float(q.strip().split(',')[7])+float(w.strip().split(',')[7])+float(e.strip().split(',')[7])+float(r.strip().split(',')[7])+float(t.strip().split(',')[7])+float(y.strip().split(',')[7])+float(u.strip().split(',')[7])+float(i.strip().split(',')[7])+float(o.strip().split(',')[7])+float(p.strip().split(',')[7]))/10
		p8=(float(q.strip().split(',')[8])+float(w.strip().split(',')[8])+float(e.strip().split(',')[8])+float(r.strip().split(',')[8])+float(t.strip().split(',')[8])+float(y.strip().split(',')[8])+float(u.strip().split(',')[8])+float(i.strip().split(',')[8])+float(o.strip().split(',')[8])+float(p.strip().split(',')[8]))/10
		p9=(float(q.strip().split(',')[9])+float(w.strip().split(',')[9])+float(e.strip().split(',')[9])+float(r.strip().split(',')[9])+float(t.strip().split(',')[9])+float(y.strip().split(',')[9])+float(u.strip().split(',')[9])+float(i.strip().split(',')[9])+float(o.strip().split(',')[9])+float(p.strip().split(',')[9]))/10
		p10=(float(q.strip().split(',')[10])+float(w.strip().split(',')[10])+float(e.strip().split(',')[10])+float(r.strip().split(',')[10])+float(t.strip().split(',')[10])+float(y.strip().split(',')[10])+float(u.strip().split(',')[10])+float(i.strip().split(',')[10])+float(o.strip().split(',')[10])+float(p.strip().split(',')[10]))/10
		p11=(float(q.strip().split(',')[11])+float(w.strip().split(',')[11])+float(e.strip().split(',')[11])+float(r.strip().split(',')[11])+float(t.strip().split(',')[11])+float(y.strip().split(',')[11])+float(u.strip().split(',')[11])+float(i.strip().split(',')[11])+float(o.strip().split(',')[11])+float(p.strip().split(',')[11]))/10
		p12=(float(q.strip().split(',')[12])+float(w.strip().split(',')[12])+float(e.strip().split(',')[12])+float(r.strip().split(',')[12])+float(t.strip().split(',')[12])+float(y.strip().split(',')[12])+float(u.strip().split(',')[12])+float(i.strip().split(',')[12])+float(o.strip().split(',')[12])+float(p.strip().split(',')[12]))/10
		p13=(float(q.strip().split(',')[13])+float(w.strip().split(',')[13])+float(e.strip().split(',')[13])+float(r.strip().split(',')[13])+float(t.strip().split(',')[13])+float(y.strip().split(',')[13])+float(u.strip().split(',')[13])+float(i.strip().split(',')[13])+float(o.strip().split(',')[13])+float(p.strip().split(',')[13]))/10
		p14=(float(q.strip().split(',')[14])+float(w.strip().split(',')[14])+float(e.strip().split(',')[14])+float(r.strip().split(',')[14])+float(t.strip().split(',')[14])+float(y.strip().split(',')[14])+float(u.strip().split(',')[14])+float(i.strip().split(',')[14])+float(o.strip().split(',')[14])+float(p.strip().split(',')[14]))/10
		p15=(float(q.strip().split(',')[15])+float(w.strip().split(',')[15])+float(e.strip().split(',')[15])+float(r.strip().split(',')[15])+float(t.strip().split(',')[15])+float(y.strip().split(',')[15])+float(u.strip().split(',')[15])+float(i.strip().split(',')[15])+float(o.strip().split(',')[15])+float(p.strip().split(',')[15]))/10
		p16=(float(q.strip().split(',')[16])+float(w.strip().split(',')[16])+float(e.strip().split(',')[16])+float(r.strip().split(',')[16])+float(t.strip().split(',')[16])+float(y.strip().split(',')[16])+float(u.strip().split(',')[16])+float(i.strip().split(',')[16])+float(o.strip().split(',')[16])+float(p.strip().split(',')[16]))/10
		p17=(float(q.strip().split(',')[17])+float(w.strip().split(',')[17])+float(e.strip().split(',')[17])+float(r.strip().split(',')[17])+float(t.strip().split(',')[17])+float(y.strip().split(',')[17])+float(u.strip().split(',')[17])+float(i.strip().split(',')[17])+float(o.strip().split(',')[17])+float(p.strip().split(',')[17]))/10
		p18=(float(q.strip().split(',')[18])+float(w.strip().split(',')[18])+float(e.strip().split(',')[18])+float(r.strip().split(',')[18])+float(t.strip().split(',')[18])+float(y.strip().split(',')[18])+float(u.strip().split(',')[18])+float(i.strip().split(',')[18])+float(o.strip().split(',')[18])+float(p.strip().split(',')[18]))/10
		p19=(float(q.strip().split(',')[19])+float(w.strip().split(',')[19])+float(e.strip().split(',')[19])+float(r.strip().split(',')[19])+float(t.strip().split(',')[19])+float(y.strip().split(',')[19])+float(u.strip().split(',')[19])+float(i.strip().split(',')[19])+float(o.strip().split(',')[19])+float(p.strip().split(',')[19]))/10
		p20=(float(q.strip().split(',')[20])+float(w.strip().split(',')[20])+float(e.strip().split(',')[20])+float(r.strip().split(',')[20])+float(t.strip().split(',')[20])+float(y.strip().split(',')[20])+float(u.strip().split(',')[20])+float(i.strip().split(',')[20])+float(o.strip().split(',')[20])+float(p.strip().split(',')[20]))/10
		p21=(float(q.strip().split(',')[21])+float(w.strip().split(',')[21])+float(e.strip().split(',')[21])+float(r.strip().split(',')[21])+float(t.strip().split(',')[21])+float(y.strip().split(',')[21])+float(u.strip().split(',')[21])+float(i.strip().split(',')[21])+float(o.strip().split(',')[21])+float(p.strip().split(',')[21]))/10
		p22=(float(q.strip().split(',')[22])+float(w.strip().split(',')[22])+float(e.strip().split(',')[22])+float(r.strip().split(',')[22])+float(t.strip().split(',')[22])+float(y.strip().split(',')[22])+float(u.strip().split(',')[22])+float(i.strip().split(',')[22])+float(o.strip().split(',')[22])+float(p.strip().split(',')[22]))/10
		
		aa.write(z.strip().split(',')[0]+','+str(p1)+','+str(p2)+','+str(p3)+','+str(p4)+','+str(p5)+','+str(p6)+','+str(p7)+','+str(p8)+','+str(p9)+','+str(p10)+','+str(p11)+','+str(p12)+','+str(p13)+','+str(p14)+','+str(p15)+','+str(p16)+','+str(p17)+','+str(p18)+','+str(p19)+','+str(p20)+','+str(p21)+','+str(p22)+'\n')
		aa.flush()
