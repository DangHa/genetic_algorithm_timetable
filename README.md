# Timetable with genetic algorithm (GA)


## Description

**Input**:

    [[Course ID, Teacher, The number of class hour, Student class, Course name, The room type need to use]]

    [[Room, The room type]

*Each week is divided into 12 blocks (from monday to friday)*

*Each block is divided into 6 class hour (both in the morning and afternoon*

**Output**:

    [[Course ID, Teacher, Room, Block position in the week, The number of class hour, Student class, Course name, room type]]



**Math model**

    - Decision variables:   A{a,b,c,d,e,f,g,h,i}  - place matrices
                                a = {Course ID}
                                b = {teacher} 
                                c = {Room} 
                                d = {1, … , 12} - The block position in the week 
                                e = {1, … , The number of class hour} 
                                f = {1, … , 6} - The beginning class hour
                                g = {Student class}
                                h = {Course Name}
                                i = {Room Type}

    - Conditions:    

        * Same teacher:       
                ∄ (p1{a1,b1,c1,d1,e1,f1,g1,h1,i1} = p2{a2,b1,c2,d2,e2,f2,g2,h2,i2} and p1,p2 ∈ A) 	       (*)
	                    ∀ (d1 == d2) and 
			            [(f1 < f2) and (f1 + e1)>f2] or [(f1 > f2) and (f2 + e2)>f1] 

        * Same room:          
                ∄ (p1{a1,b1,c1,d1,e1,f1,g1,h1,i1} = p2{a2,b2,c1,d2,e2,f2,g2,h2,i2} and p1,p2 ∈ A)            (**)
	                    ∀ (d1 == d2) and 
			            [(f1 < f2) and (f1 + e1)>f2] or [(f1 > f2) and (f2 + e2)>f1]

        * Same student class: 
                ∄ (p1{a1,b1,c1,d1,e1,f1,g1,h1,i1} = p2{a2,b2,c2,d2,e2,f2,g1,h2,i2} and p1,p2 ∈ A)            (***)
	                    ∀ (d1 == d2) and (h1 != h2)
			            [(f1 < f2) and (f1 + e1)>f2] or [(f1 > f2) and (f2 + e2)>f1]

    - Target:

        * ∃ A{a,b,c,d,e,f}   Satisfies  (*), (**) and (***)

**The progress of algorithm**

![](https://gitlab.com/ha_algorithm/timetable/uploads/fa77d61efad4fc50588542cb1323f4bd/image.png)


## How to run 
    python3 src/main.py