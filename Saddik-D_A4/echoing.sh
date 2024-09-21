echo "Let’s see who is logged into the system: $(who)"
echo "For $USER, the home directory is $HOME"

#Activity 2: Working with positional arguments
$1
$2

echo "My name is $1 and I have \$$2 in my wallet."

#Activity 3: Math time
mathvar1=$((1+5))
echo "Variable 1 is $mathvar1."
mathvar2=$((mathvar1 *20))
echo $mathvar2
mathvar3=$((10))
echo $mathvar3
mathvar4=$(($mathvar1 *($mathvar2 + $mathvar3)))
echo $mathvar4


#Activity 4: More math. Working with floating-point solution
floating=$(echo "scale=3; 4.5/1.7" | bc -l)
echo "Our floating variable is $floating"
