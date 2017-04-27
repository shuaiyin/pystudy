# -*- coding: utf-8 -*-


def draw_pic(figsizex,figsizey,draw_dict,color_count,ylimt_bot,ylim_top,title="this is the title",xlabel="this is xlabel",ylabel="this is y label"):
	print draw_dict
	plt.figure(figsize=(figsizex,figsizey))
	x = draw_dict['xval']
	color_list = choose_some_color(cnames,color_count)
	color_num = 0
	print "the length of xval is " + str(len(draw_dict['xval']))
	for key in draw_dict:
		print "the length of y is " + str(len(draw_dict[key]))
		if key == 'xval': continue
		linewidth = 4 if key in ('totalStatistic','totalDistinctStatistic') else 2
		y = draw_dict[key]
		print y
		plt.gcf().autofmt_xdate()#make x datetime show beautiful
		try:
			plt.plot(x,y,color=color_list[color_num],label=key,linewidth=linewidth)
		except Exception,e:
			print e

		color_num += 1 
	plt.ylim(ylimt_bot,ylim_top)#set the limit of y xlia 
	plt.legend(loc="top left",shadow=True)#set the tuli 
	plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	# plt.savefig("./a.png")
	plt.show()