#!/usr/bin/env bash

# 压测脚本模板中设定的压测时间应为20秒
export jmx_template="iInterface"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"
#运行shell命令的时候，不同的平台对不同shell命令的格式有不同要求，通过这个变量拿到当前的平台是linux还是mac
export os_type=`uname`

# 需要在系统变量中定义jmeter根目录的位置，如下
export jmeter_path="/Users/jinlianfu/Downloads/apache-jmeter-5.2.1"

echo "自动化压测开始"

# 压测并发数列表
thread_number_array=(10 20 30)
for num in "${thread_number_array[@]}"
do
    # 生成对应压测线程的jmx文件
    export jmx_filename="${jmx_template}_${num}${suffix}"
    #jtl，压测结果文件
    export jtl_filename="test_${num}.jtl"
    #压测报告路径的名字
    export web_report_path_name="web_${num}"

    #环境清理：如果存在的话先删掉
    rm -f ${jmx_filename} ${jtl_filename}
    rm -rf ${web_report_path_name}

    #只是内容的复制、不含文件名称的复制？实际原始的压测脚本的内容复制到jmx_filename的内容中
    cp ${jmx_template_filename} ${jmx_filename}
    echo "生成jmx压测脚本 ${jmx_filename}"

    #生成对应并发数的压测脚本，如果是mac系统走逻辑1格式，jmx_filename变成了带实际并发数的jmx文件
    if [[ "${os_type}" == "Darwin" ]]; then
        sed -i "" "s/thread_num/${num}/g" ${jmx_filename}
    else
        sed -i "s/thread_num/${num}/g" ${jmx_filename}
    fi

    # JMeter 静默压测
    ${jmeter_path}/bin/jmeter -n -t ${jmx_filename} -l ${jtl_filename}

    # 生成Web压测报告
    ${jmeter_path}/bin/jmeter -g ${jtl_filename} -e -o ${web_report_path_name}

    #清理环境
    rm -f ${jmx_filename} ${jtl_filename}
done
echo "自动化压测全部结束"