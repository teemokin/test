cd E:\pongocode\flaskexam

git remote remove origin
git remote add origin https://github.com/pongocode/flaskexam.git
git remote set-url origin "https://pongocode@github.com/pongocode/flaskexam.git"

git add .
git commit -m "auto push"
git push -f origin master


@pause
