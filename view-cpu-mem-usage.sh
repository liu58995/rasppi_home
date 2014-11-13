#!/bin/bash
#view the cpu and memory consumption of each user at the current time
#three options : --reverse --mem --cpu
#learning points, string comparing in shell

function view_consumption(){
    ps aux|grep -v 'PID' | sed 's/[ ][ ][ ]*/ /g' | cut -d " " -f1-4 | sort |awk '
    BEGIN{
        user_id = "None"
        cpu_usage = 0
        mem_usage = 0
    }
    {
        if(user_id == $1){
            cpu_usage += $3
            mem_usage += $4
        }else{
            if(user_id != "None"){
                printf("%16s     %4.1f    %4.1f\n", user_id, cpu_usage, mem_usage);
            }
            user_id = $1
            cpu_usage = $3
            mem_usage = $4
       }
    }'
}

if [ "$1"x = "--mem"x ]; then
     key="-k 3 -n"
elif [[ "$1" = "--cpu" ]];then
     key="-k 2 -n"
fi

if [[ "$1" = "--reverse" ]]||[[ "$2" = "--reverse" ]]; then
   reverse="-r"
fi

echo "List the cpu and mem usage of all the users"
echo "           USERID      CPU     MEM"

view_consumption|sort $key $reverse

   
    
