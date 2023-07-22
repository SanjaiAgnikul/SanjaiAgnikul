
def ch0_offset_calc():
    channel = [0, 0, 0, 0, 0, 0, 0, 0]
    # a = 0
    do_once = [1, 1, 1, 1, 1, 1, 1, 1]
    
    sensors = 8  
    
    skip_lines = 1
    
    element_counter = 0

    calib_ch0 = [0, 0, 0, 0, 0, 0, 0, 0]

    line_number = 0

    header_ch0 = ["P_C_PT_LOX_inj" , "P_F_PT_ATF_inj" ,"P_E_PT_CC_1" ,"P_M_PT_inj" ,"P_G_PT_inj" , "P_I_PT_1" ,"P_I_PT_2" , "P_R_PT_RCS_2"]
    with open("channel0.log", "r") as csv_file:
        #     csv_reader = csv.reader(csv_file)
        for line in csv_file.readlines():
            if line_number < skip_lines:
                line_number += 1
                continue
            splitted = line.split(",")#.strip()
            #print(splitted)
            for i in range(0, len(splitted)):
                if i == 0:
                    continue
                if i == 9:
                    continue
                if do_once[i - 1] == 1:
                    channel[i - 1] = int(splitted[i])
                    do_once[i - 1] = 0
                    element_counter = 1
                    continue
                # print(channel[i-1])
                channel[i - 1] = (element_counter / (element_counter + 1)) * channel[i-1] + (1 / (element_counter + 1)) * int(splitted[i])
                calib_ch0[i - 1] = 9830.4-channel[i - 1] 
                
        element_counter += 1


    with open('calib_offsetch0.csv','w') as f:
        for row in range(sensors):
           f.write(header_ch0[row] )
           f.write(',')
           f.write(str(calib_ch0[row]))
           f.write(',' + '0' + ',' + '0')
           f.write(',')
           f.write('0' + ',' + '0')
           f.write('\n')
            # channel_0[i - 1] = (1 - weight) * channel_0[i - 1] + weight * int(
            #     splitted[i]
            # )
        

def ch2_offset_calc():
    channel = [0, 0, 0, 0, 0, 0, 0, 0]
    # a = 0
    do_once = [1, 1, 1, 1, 1, 1, 1, 1]
    
    sensors = 8  
    
    skip_lines = 1
    
    element_counter = 0

    calib_ch2 = [0, 0, 0, 0, 0, 0, 0, 0]

    line_number = 0
    
    counter = 1

    header_ch2 = ["P_F_PT_ATF_Press_Tank" , "P_F_PT_ATF_Tank" ,"P_F_PT_ATF_Press" ,"P_C_PT_LOX_Press_Tank" ,"P_C_PT_LOX_Tank" , "P_C_PT_LOX_Press" ,"P_R_PT_RCS_1" , "P_C_LS_LOX_Tank"]
    with open("channel2.log", "r") as csv_file2:
        #     csv_reader = csv.reader(csv_file)
        for line in csv_file2.readlines():
            if line_number < skip_lines:
                line_number += 1
                continue

            splitted = line.split(",")#.strip()
            # print(splitted)
            #print(splitted)
            for i in range(0, len(splitted)):
                if i == 0:
                    continue
                if i == 9:
                    continue
                if do_once[i - 1] == 1:
                    channel[i - 1] = int(splitted[i])
                    do_once[i - 1] = 0
                    element_counter = 1
                    
                    continue
               
                
                channel[i - 1] = (element_counter / (element_counter + 1)) * channel[i-1] + (1 / (element_counter + 1)) * int(splitted[i])

                calib_ch2[i - 1] = 9830.4-channel[i - 1]  
            # channel_0[i - 1] = (1 - weight) * channel_0[i - 1] + weight * int(
            #     splitted[i]
            # )
          
        element_counter += 1
    

    with open('calib_offsetch2.csv','w') as f:
        for row in range(sensors):
           f.write(header_ch2[row] )
           f.write(',')
           f.write(str(calib_ch2[row]))
           f.write(',' + '0' + ',' + '0')
           f.write(',')
           f.write('0' + ',' + '0')
           f.write('\n')
    
ch0_offset_calc()
ch2_offset_calc()

exit()

# Moving average. avg = w*a[n]+(1-w)*a[n+1]
import pandas as pd

# import csv

# with open("channel0.log", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print((line[2]))
df = pd.read_csv("channel0.log")
print(df)
val = df[
    [
        "sensor1",
        "sensor2",
        "sensor3",
        "sensor4",
        "sensor5",
        "sensor6",
        "sensor7",
        "sensor8",
    ]
].mean(axis=0, numeric_only=True, skipna=True)
print(val)
val.to_csv("/home/sanjaik/Downloads/calib_offset.csv")


## Open a file.
## Read line by line.
## Split each line into columns .split(",")
##
