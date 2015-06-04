require 'fox16'
require 'date'

include Fox

class TableWindow < FXMainWindow

  def initialize(app)

#data geeneration logic 
ip = []
pro = []
error = []
ran =[]
days = []
months = []
years = []
hour =[]
mins = []
secs = []
gmts = []
method = []
web =[] 
pc = []
eng_type = []
lib_type = []
browser = []
ver =[]
filename = ARGV.first
count =0
browser_cnt = [0,0,0,0]
method_cnt = [0,0,0,0]
use_count = [0,0]
#txt = open(filename)
fileopen = 'database.txt'
fileopen1 = 'summary.txt'
target = open(fileopen, 'w')
target1 = open(fileopen1, 'w')
#print "Content is :"

txt=File.open(filename).read
txt.gsub!(/\r\n?/, "\n")

txt.each_line do |line_one|
count = count + 1
#target.write("#{line_one}\n")  
#print "#{line_one}\n"

#line_one = txt.lines.first

#split Line
input_string = line_one.partition('- -').last
#target.write("#{input_string} \n")
#print "#{input_string} \n"
#extract Ip_Address
ip_address = line_one.rpartition("- -").first

	(ip ||=[]) << ip_address

target.write("#{ip_address} \n")
#print "#{ip_address} \n"

str1_markerstring = "\\\["
str2_markerstring = "\\\]"

inp = input_string[/#{str1_markerstring}(.*?)#{str2_markerstring}/m,1]

#print "#{inp} \n"

day = inp.partition("\/").first

	(days ||=[]) << day

target.write("#{day} \n")
#print "#{day} \n"

inp1 = inp.partition("\/").last
month = inp1.partition("\/").first

	(months ||=[]) << month

target.write("#{month} \n")
#print "#{month} \n"

inp2 = inp1.partition("\/").last
year = inp2.partition(":").first

	(years ||=[]) << year

target.write("#{year} \n")
#print "#{year} \n"

inp3 = inp2.partition(":").last
hrs = inp3.partition(":").first

	(hour ||=[]) << hrs

target.write("#{hrs} \n")
if hrs.match("22") 
    use_count[0] = use_count[0] + 1
elsif hrs.match("0") && hrs.match("8")
    use_count[0] = use_count[0] + 1
else
    use_count[1] = use_count[1] + 1
end
#print "#{hrs} \n"

inp4 = inp3.partition(":").last
min = inp4.partition(":").first

	(mins ||=[]) << min

target.write("#{min} \n")
#print "#{min} \n"

inp5 = inp4.partition(":").last
sec = inp5.partition("-").first

	(secs ||=[]) << sec

target.write("#{sec} \n")
#print "#{sec} \n"

inp6 = inp5.partition("-").last
gmt = inp6

	(gmts ||=[]) << gmt

target.write("#{gmt} \n")
#print "#{gmt} \n"

str1_markerstring = "\\\""
str2_markerstring = "\\\""

man = input_string[/#{str1_markerstring}(.*?)#{str2_markerstring}/m,1]

#print "#{inp.split(' ')[0]} \n"
var=0
if man.upcase.match(/GET/)
        (method ||=[]) << "GET"
        method_cnt[0] = method_cnt[0] + 1
     	target.write("GET\n")
	var =1
	#print "GET\n"
elsif man.upcase.match(/POST/)
        (method ||=[]) << "POST"
        method_cnt[1] = method_cnt[1] + 1
        target.write("POST\n")
	#print "POST\n"
	var = 1
elsif man.upcase.match(/HEAD/)
        (method ||=[]) << "HEAD"
        method_cnt[2] = method_cnt[2] + 1
        target.write("HEAD\n")
	#print "POST\n"
	var = 1
end
if var==0
	(method ||=[]) << "-"
       method_cnt[3] = method_cnt[3] + 1
end
website = man.split(' ')[1]

	(web ||=[]) << website

target.write("#{website}\n")
#print "#{website}\n"

protocol = man.split(' ')[2]

	(pro ||=[]) << protocol

target.write("#{protocol}\n")
#print "#{protocol}\n"

error_code = input_string.partition("\"\s").last.partition("\"").first.split(' ')[0]

	(error ||=[]) << error_code

target.write("#{error_code}\n")
#print "#{error_code}\n"

ran_no = input_string.partition("\"\s").last.partition("\"-\"").first.split(' ')[1]

	(ran ||=[]) << ran_no

target.write("#{ran_no}\n")
#print "#{ran_no}\n"

	(eng_type ||=[]) << input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").first

target.write("#{input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").first} \n")

	(ver ||=[]) << input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").last

target.write("#{input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").last} \n")
if input_string.rpartition("\s\"").last.upcase.match(/COMPATIBLE/)
	#target.write("#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1]}\n")
	
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1]}\n"
	#print "#{input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").first} \n"
	#print "#{input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").last} \n"
	unless input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].nil?	
		target.write("#{input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].split('; ')[0]}\n")
		target.write("#{input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].split('; ')[1]}\n")
		target.write("#{input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].split('; ')[2]}\n")
		#print "#{input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].split('; ')[0]}\n"			
		#print "#{input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].split('; ')[1]}\n"
		#print "#{input_string.rpartition("\s\"").last[/\((.*?)(\)|\")/m,1].split('; ')[2]}\n"
	end
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1].blank?}\n"
	#unless input_string.rpartition("\s\"").last[/\((.*?)\"/m,1].nil?
	#	print "#{input_string.rpartition("\s\"").last[/\((.*?)\"/m,1].split('; ')[0]}\n"			
	#	print "#{input_string.rpartition("\s\"").last[/\((.*?)\"/m,1].split('; ')[1]}\n"
	#	print "#{input_string.rpartition("\s\"").last[/\((.*?)\"/m,1].split('; ')[2]}\n"
	#end
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1].split('; ')[3]}\n"	
end
	
	#target.write("#{input_string.rpartition("\s\"").last.upcase}\n")
	#print "#{input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").first} \n"
	#print "#{input_string.rpartition("\s\"").last.split(' ')[0].partition("\/").last} \n"
	#print input_string.rpartition("\s\"").last.upcase
	fant =0	
	if input_string.rpartition("\s\"").last.upcase.match(/MACINTOSH/)
        	(pc ||=[]) << "Mac PC"
		fant=1
		target.write("Mac PC\n")		
		#print "Mac PC\n"
	
	end
	if input_string.rpartition("\s\"").last.upcase.match(/WINDOWS/)
        	(pc ||=[]) << "WINDOWS PC"
		fant = 1
		target.write("WINDOWS PC\n")	
		#print "WINDOWS PC\n"
	
	end
	if fant ==0
		(pc ||=[]) << "-"
		fant =0
	end

    fant1 =0
    if input_string.rpartition("\s\"").last.upcase.match(/APPLEWEBKIT/)
        (lib_type ||=[]) << "APPLEWEB kIT"
        fant1=1
		target.write("APPLEWEB kIT USED\n")
		#print "APPLEWEB kIT USED\n"
	end
	if input_string.rpartition("\s\"").last.upcase.match(/GECKO/)
        (lib_type ||=[]) << "GECKO"
        fant1=1
		target.write("GECKO USED\n")
		#print "GECKO USED\n"
	end
    if fant1 ==0
		(lib_type ||=[]) << "-"
		fant1 =0
	end
    fant2 =0 
    if input_string.rpartition("\s\"").last.upcase.match(/CHROME/)
        (browser ||=[]) << "Chrome"
        fant2=1
        browser_cnt[0] = browser_cnt[0] + 1
		target.write("CHROME used\n")
		#print "CHROME used\n"
	end
	if input_string.rpartition("\s\"").last.upcase.match(/SAFARI/)
        (browser ||=[]) << "Safari"
        fant2=1
        browser_cnt[1] = browser_cnt[1] + 1
		target.write("SAFARI used\n")
		#print "SAFARI used\n"	
	end
    if input_string.rpartition("\s\"").last.upcase.match(/OPERA/)
        (browser ||=[]) << "Opera"
        fant2=1
        browser_cnt[2] = browser_cnt[2] + 1
		target.write("OPERA used\n")
		#print "SAFARI used\n"	
	end
    if fant2 ==0
		(browser ||=[]) << "-"
		fant2 =0
        browser_cnt[3] = browser_cnt[3] + 1
	end
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1].split('; ')[0]}\n"			
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1].split('; ')[1]}\n"
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1].split('; ')[2]}\n"
	#print "#{input_string.rpartition("\s\"").last[/\((.*?)\)/m,1].split('; ')[3]}\n"


target.write("\n")
#print "*************************************\n"
end
target.close()
#print "#{ip.length}\n"
#print "#{pro.length}\n"
#print "#{error.length}\n"
#print "#{ran.length}\n"
#print "#{days.length}\n"
#print "#{months.length}\n"
#print "#{years.length}\n"
#print "#{hour.length}\n"
#print "#{mins.length}\n"
#print "#{secs.length}\n"
#print "#{gmts.length}\n"
#print "#{method.length}\n"
#print "#{web.length}\n"
#print "#{pc.length}\n"
#print "#{eng_type.length}\n"
#print "#{ver.length}\n"
#print "#{count}\n"

print "Broser Count : \n"
print "************\n"
target1.write("Broser Count : \n************\n")
print "Chrome : #{browser_cnt[0]}\nSafari : #{browser_cnt[1]}\nOpera : #{browser_cnt[2]}\nOthers : #{browser_cnt[3]}\n"
print "************\n"
target1.write("Chrome : #{browser_cnt[0]}\nSafari : #{browser_cnt[1]}\nOpera : #{browser_cnt[2]}\nOthers : #{browser_cnt[3]}\n************\n")
print "Total Links Hit : #{web.length}\n"
print "************\n"
target1.write("Total Links Hit : #{web.length}\n************\n")
print "GET : #{method_cnt[0]}\nPOST : #{method_cnt[1]}\nHEAD : #{method_cnt[2]}\n"
print "************\n"
target1.write("GET : #{method_cnt[0]}\nPOST : #{method_cnt[1]}\nHEAD : #{method_cnt[2]}\n************\n")
print "Links Hit \nDuring Day : #{use_count[1]*100/web.length}%\nDuring Night : #{use_count[0]*100/web.length}%\n"
print "************\n"
target1.write("Links Hit \nDuring Day : #{use_count[1]*100/web.length}%\nDuring Night : #{use_count[0]*100/web.length}%\n************\n")
target1.close
    # Call the base class initializer first
    super(app, "Table Widget Test", :opts => DECOR_ALL)

# Separator
    FXHorizontalSeparator.new(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X|SEPARATOR_GROOVE)
  
    # Contents
    contents = FXVerticalFrame.new(self, LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
    
    frame = FXVerticalFrame.new(contents,
      FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y, :padding => 0)

# Table
    @table = FXTable.new(frame,
      :opts => TABLE_COL_SIZABLE|TABLE_ROW_SIZABLE|LAYOUT_FILL_X|LAYOUT_FILL_Y,
      :padding => 2)
      
    @table.visibleRows = 20
    @table.visibleColumns = 8

    @table.setTableSize(2778, 12)

    @table.setBackColor(FXRGB(255, 255, 255))
    

	headers = []
	(headers ||=[]) << "ip"
	(headers ||=[]) << "date"
	(headers ||=[]) << "time"
	(headers ||=[]) << "method"
	(headers ||=[]) << "website"
	(headers ||=[]) << "protocol"
	(headers ||=[]) << "error code"
	#(headers ||=[]) << "ran"
	(headers ||=[]) << "eng_type"
	(headers ||=[]) << "ver"
	(headers ||=[]) << "pc"
    (headers ||=[]) << "browser"
    (headers ||=[]) << "Web-Kit"
	# Initialize column headers
	 
    (0...12).each  { |c| @table.setColumnText(c, headers[c]) }
	
    
    # Initialize row headers
    (0...2778).each { |r| @table.setRowText(r, "#{r+1}")}
 
        c=0
 	    (0..2777).each do |r|
            @table.setItemText(r, c, ip[r])
        end
        c=1
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{days[r]}-#{months[r]}-#{years[r]}")
        end
        c=2
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{hour[r]}:#{mins[r]}:#{secs[r]} - #{gmts[r]}")
        end
        c=3
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{method[r]}")
        end
        c=4
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{web[r]}")
        end
        c=5
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{pro[r]}")
        end
        c=6
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{error[r]}")
        end
        #c=7
 	    #(0..2777).each do |r|
            #@table.setItemText(r, c, "#{ran[r]}")
       # end
        c=7
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{eng_type[r]}")
        end
        c=8
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{ver[r]}")
        end
        c=9
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{pc[r]}")
        end
        c=10
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{browser[r]}")
        end
        c=11
 	    (0..2777).each do |r|
            @table.setItemText(r, c, "#{lib_type[r]}")
        end
	#(0..2777).each do |r|
      #(6..10).each do |c|
        #@table.setItemText(r, c, "r:#{r} c:#{c}")
      #end
    #end
end

# Create and show this window
  def create
    super
    show(PLACEMENT_SCREEN)
  end
end

# Start the whole thing
if __FILE__ == $0
  # Make application
  application = FXApp.new("TableApp", "FoxTest")
  
  # Make window
  t = TableWindow.new(application)
  
  # Create app
  application.create
  
  # Run
  application.run
end
