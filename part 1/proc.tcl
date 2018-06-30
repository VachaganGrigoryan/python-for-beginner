# proc sum {} {
# 		#  Process data file
# 		set fp [open "test.txt" r]
# 		set file_data [read $fp]
# 		set data [split $file_data "\n"]
# 		foreach line $data {
# 				set c [expr $line]
#     		puts "  $c   "
# 		}
# 		close $fp
# }

proc sub {a} {
    set c [expr $a]
    if {$c == 24} {
    	puts " $a  =  $c"
    }

}

eval $argv;