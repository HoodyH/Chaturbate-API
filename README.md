# Chaturbate API

Commands framework to handle text commands in a easy way.
#### Install
pip install git+https://git@github.com/SpinPool/Chaturbate-API.git@0.0.1

####Example Base
It will query in the home page https://c-urbate.com/
```python
    from chaturbate_api import ChaturbateSearch, ChatrubateCam, Type, Tag

    cams = ChaturbateSearch().search()
    
    # Show the results
    for cam in cams.results:
        cam: ChatrubateCam
        print(
                cam.gender.name.title(),
                cam.age,
                cam.url,
                cam.location, 
                cam.uptime_min, 
                cam.spectators
            )
```
Inside **.search()** you can specify:
+ **gender** the gender of the cam (male, female, etc)
+ **query** a keyword to find in username on the site
+ **nr_pages** the number of pages where search in
```python
    cams = ChaturbateSearch().search(
        gender=Type.FEMALE,
        query="cats",
        nr_pages=10
    )
    out = cams.results
```
####Example With Tag
Same as before but you can specify a tag and it will query here:
https://c-urbate.com/tag/tag_name/
+ **tag** one of the tags defined by th user
```python
    cams = ChaturbateSearch().search_tag(
        gender=Type.FEMALE,
        tag=Tag.CUTE,
        query="cats",
        nr_pages=10
    )
    out = cams.results
```
You can use the default Tags or you can build your custom one
```python
    MyTag = Enum('MyTag', {'CUSTOM': 'cute/'}) # you MUST put the / at the end
    cams = ChaturbateSearch().search_tag(
        tag=MyTag.CUSTOM,
        gender=Type.FEMALE
    )
    out = cams.results
```



####Example With the Filter  
The ChaturbateSearch.search() and ChaturbateSearch.search_tag() methods returns a ChaturbateSearch istance 

So you can se that to filter the results
the **.filterpy()** take as parameters:
+ **gender** the gender of the cam (male, female, etc)
+ **age** a keyword to find in username on the site
+ **uptime_min** min of uptime of the show
+ **spectators** the number of spectators in the show
You must use lambda parameters to filter the data
```python
    cams = ChaturbateSearch().search()

    cams = cams.filter_by(
        gender=Type.TRANS,
        age=lambda age: True if 65 <= age <= 85 else False,
        uptime_min=lambda uptime_min: True if 30 <= uptime_min <= 200 else False,
        spectators=lambda spectators: True if 1 <= spectators <= 20 else False,
    )
    out = cams.filtered_results
```
#### NB How filtered_results works
When you filter some data the content will be available in **filtered_results** 
and **results** will stay the same, so you can filter the data as many times you want!
without make a new call to the site.

#DISCLAIMER
this are NOT official api. I don't take any responsibility for what you do with this code.

Use at your own risk
