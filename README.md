# Timetable with genetic algorithm (GA)

### Description

**Input**:
    [[Mã lớp, Giảng viên, Số tiết]]
    [[Phòng học, Buổi, SoTietConLai]]
**Output**:
    [[Mã lớp, Giảng viên, Phòng, Buổi, Số tiết]]

*Each week is divided into 12 blocks (from monday to friday)*
*Each block is divided into 6 periods (both in the morning and afternoon*

**Math model**
    - Decision variables:   `Place matrices`  Aa,b,c,d,e,f 
                                                a = {Mã lớp}
                                                b = {1,…., Số giảng viên} 
                                                c = {1, … , Số Phòng học} 
                                                d = {1, … , 12} - Số buổi trong tuần 
                                                e = {1, … , Số tiết của môn học}
                                                f = {1, … , 6} - Tiết bắt đầu
    - Conditions:    
        * Same b1:  ∄ (A{a1,b1,c1,d1,e1,f1}  = A{a2,b1,c2,d2,e2,f2}) 	         (*)
	                    ∀ (d1 = d2) and 
			            [(f1 < e2) and (f1 + e1)>f2] or [(f1 > f2) and (f2 + e2)>f1] 
        * Same c1:  ∄ (A{a1,b1,c1,d1,e1,f1}   = A{a2,b2,c1,d2,e2,f2})            (**)
	                    ∀ (d1 = d2) and 
			            [(f1 < f2) and (f1 + e1)>f2] or [(f1 > f2) and (f2 + e2)>f1]

    - Target:
        * ∃( A{a1,b1,c1,d1,e1,f1} = A{a1,b2,c2,d2,e2,f2})  Satisfies  (*) and (**)


### How to run 
    python3 src/main.py