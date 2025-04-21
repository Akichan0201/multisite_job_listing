## Scrape multi-site job listing
well hello there👋. So today i'm gonna show you the next project. so what todo is i have to scrape from multi-site for job, like from linkedIn, Jobstreet, Glints,and other site.
because there is so many list of jobs, so i'm gonna get 5000+ data of listing. because there is so many ways to scrape i'm gonna use Python cause it much easier to learn than other language
(for me).

i will separate it into some different files for each link and function so we don't have to change every code to every site

### What to do?
in here i will use 2 modules for scrape cause we didn't know which one can be more effective to scrape.

**1. make the file for every function from inisiation every module, links every site, and for export data(to csv or excel)**
first, make inisiate the bs4 and selenium so from that we can call in another file. after that make a new file to get/extract data from every links. Try it with one site first so you can figure out how the output would look like. In here i would get the HTML first because i will get the data from it. and after that last you can make a new file again for export function.

**2. Always give the parameter for each function**
why? cause we can know which one the function we called.  it would be much easier for us to know specifically about the function.

if you still confused just check out the code that i made. for file _main.py_ you can change it to anaother links based on the website you choose.
   
