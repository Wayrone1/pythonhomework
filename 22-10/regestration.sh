#!/bin/bash 
while [[ 1 -eq 1 ]]
do
    rg=0  #     любая переменная, в заисимости от который мы решаем дальнейшие действия
    echo 'Введите логин: '
    read ul
    while read login
    do 
        if [[ $ul == $login ]] # юзер = логин 2 строки 
        then 
            rg=1 
        fi
    done < database # считыывает с датабэйса 
    if [[ $rg -eq 1 ]] #значение 
    then 
        echo "Логин занят"
    else
        echo "Введите пароль"
        read -s password  #-s скрывает пароль 
        echo "$ul" >>database 
        echo "$password" >>database
        break 

    fi
done





