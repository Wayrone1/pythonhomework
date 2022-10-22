#!/bin/bash 

while [[ 1 -eq 1 ]]
do
    av=0  # 
    echo 'Введите логин: '
    read ul
    while read login 
    do 
        if [[ $av -eq 2 ]]  #если логин есть в базе данных берем пароль из следующей строчки 
        then 
            pass=$login
            av=1 
        fi
        if [[ $ul == $login ]] # юзер = логин 
        then 
            av=2 
        fi
    done <database # считыывает с датабэйса 
    if [[ $av -eq 1 ]] 
    then 
        echo "Введите пароль:"
        read -s password
        if [[ $password == $pass ]]
        then 
            echo "Вы авторизовались!"
            break
        else
            echo "Вы ввели неверный пароль!!!"
            break 
        fi
    else 
        echo "Такого логина нет в базе данных!"
    fi

done



