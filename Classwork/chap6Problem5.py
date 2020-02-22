#Creates an html file based on input
name = input("Enter your name: ")
string = input("Enter a sentence: ")

write_htmlPage = open("webpage.html", "w")

write_htmlPage.write("<html>\n")
write_htmlPage.write("<head>\n")
write_htmlPage.write("<title>" + name + "'s Webpage" + "</title>\n")
write_htmlPage.write("</head>\n")
write_htmlPage.write("<body>\n")
write_htmlPage.write("<h1>" + string + "</h1>\n")
write_htmlPage.write("</body>\n")
write_htmlPage.write("</html>\n")

write_htmlPage.close()
