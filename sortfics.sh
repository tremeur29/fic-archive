#!/usr/bin/env bash

for i in {1..500}
do
    if [[ $i -lt 10 ]]
    then
        ficstring="00$i"
    else
        if [[ $i -lt 100 ]]
        then
            ficstring="0$i"
        else
            ficstring="$i"
        fi
    fi
    if compgen -G "texts/${ficstring}.*" > /dev/null
    then
        if test -f "originalsmeta/${ficstring}.py"
        then
            if grep -q "^locked = True" "originalsmeta/${ficstring}.py"
               then
                   builddir="secret"
            else
                if grep -q "^locked = False" "originalsmeta/${ficstring}.py"
                then
                    builddir="files"
                fi
            fi
        else
            if test -f "translationsmeta/${ficstring}.py"
            then
                if grep -q "^locked = True" "translationsmeta/${ficstring}.py"
                then
                    builddir="secret"
                else
                    if grep -q "^locked = False" "translationsmeta/${ficstring}.py"
                    then
                        builddir="files"
                    fi
                fi
            else
                builddir="null"
            fi
        fi
        if [ ${builddir} != "null" ]
        then
            if test -f "texts/${ficstring}.html"
            then
                if ! test -f "build/${builddir}/${ficstring}.html"
                then
                    mv "texts/${ficstring}.html" "build/${builddir}/"
                fi
            fi
            if test -f "texts/${ficstring}.pdf"
            then
                if ! test -f "build/${builddir}/${ficstring}.pdf"
                then
                    mv "texts/${ficstring}.pdf" "build/${builddir}/"
                fi
            fi
            if test -f "texts/${ficstring}.epub"
            then
                if ! test -f "build/${builddir}/${ficstring}.epub"
                then
                    mv "texts/${ficstring}.epub" "build/${builddir}/"
                fi
            fi
        fi
    fi
done
