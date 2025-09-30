if [[ -v WORKSHOP ]]; then
    echo "WORKSHOP_DIRECTORY already exists, leaving i>
else
    export WORKSHOP_DIRECTORY="/home/fuzzy/GitHub/work>
fi

alias create=$WORKSHOP_DIRECTORY/scripts/create.py
alias compile=$WORKSHOP_DIRECTORY/scripts/compile.py
alias run=$WORKSHOP_DIRECTORY/scripts/run.py

export getpkgtoolscript="$WORKSHOP_DIRECTORY/scripts/p>

	

