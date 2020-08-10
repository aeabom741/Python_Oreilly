single = {'green':'go',"yellow":'go faster','red':'smile for the camera'}
save_single = single
single['blue'] = 'confuse everyone'
print(save_single)

print('-------------------------------------------------------------')

single = {'green':'go',"yellow":'go faster','red':'smile for the camera'}
original_single = single.copy()
single['blue'] = 'confuse eveyone'
print(single)
print(original_single)