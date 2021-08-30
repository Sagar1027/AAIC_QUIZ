import json
f = open('quiz.json')
jfile = json.load(f)

sub = jfile["quiz"]
list = []
for key in sub.keys():
	list.append(key)

print("Select any subject :")
for i in range (len(list)):
	print(i+1,".",list[i])
que=input()

print()
i=1
arr = []
c1 ="Your answer is correct."
c2 = "Your answer is wrong."
c3 = "\nCorrect Answer is: "
while True:
	try:
		print("Que. {}:".format(i), jfile["quiz"][que]["q{}".format(i)]["question"])
		opt = jfile["quiz"][que]["q{}".format(i)]["options"]
		for j in range (4):
			print(opt[j])
		ans = input("\nEnter your answer:")
		ANSWER = jfile["quiz"][que]["q{}".format(i)]["answer"]
		if ans==ANSWER:
			arr.append(c1)
		else:
			arr.append(c2+c3+ANSWER)
		i+=1
		
	except:
		break
print('\nResult:')
for k in range(1,i):
	print('Que. {}: '.format(k), arr[k-1])
	print()
