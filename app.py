from browser import document as doc
from browser import alert, ajax, html,alert,console 


#Picks
def rover_pick(ev):
    global rover
    for opt in doc['rover']:
        if opt.selected:
            if opt.value == 'curiosity':
                rover = 'curiosity'
            elif opt.value == 'opportunity':
                rover = 'opportunity' 
            elif opt.value == 'spirit':
                rover = 'spirit'
            print(rover)
doc['btn'].bind('click', rover_pick) 

def cam_pick(ev):
    global cam
    global rover
    for opt in doc['camera']:
        if opt.selected:
            if opt.value == 'FHAZ':
                cam = 'FHAZ'
            elif opt.value == 'RHAZ':
                cam = 'RHAZ'
            elif opt.value == 'MAST':
                cam = 'MAST'
            elif opt.value == 'CHEMCAM':
                cam = 'CHEMCAM'
            elif opt.value == 'MAHLI':
                cam = 'MAHLI'
            elif opt.value == 'MARDI':
                cam = 'MARDI'
            elif opt.value == 'NAVCAM':
                cam = 'NAVCAM'
            elif opt.value == 'PANCAM':
                cam = 'PANCAM'
            elif opt.value == 'MINITES':
                cam = 'MINITES' 
            print(cam)
doc['btn'].bind('click', cam_pick) 

def date_pick(ev):
    global sol
    sol = doc['date'].value
doc['btn'].bind('click', date_pick)

#validações
def valid_picks(ev):
    global sol
    global rover
    global cam
    if any(i not in '0123456789' for i in sol):
        alert('sol should be only numbers. It is the martian days.')
        return False

    if rover == "curiosity":
        if cam == "PANCAM":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "MINITES":
            alert('this rover is not equiped with this camera')
            return False
        else:
            return True

    elif rover == "spirit":
        if cam == "MAST":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "CHEMCAM":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "MAHLI":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "MARDI":
            alert('this rover is not equiped with this camera')
            return False
        else:
            return True

    elif rover == "opportunity":
        if cam == "MAST":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "CHEMCAM":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "MAHLI":
            alert('this rover is not equiped with this camera')
            return False
        elif cam == "MARDI":
            alert('this rover is not equiped with this camera')
            return False
        else:
            return True

doc['btn'].bind('click',valid_picks)


#pega o data e joga na tela em forma de grid
def on_complete(req):
    import json
    data = json.loads(req.text)
    for i in data['photos']:
        doc['output'] <= html.IMG(src=i['img_src'], Class='pic')
#Ajax Call
def search(ev):
     #setting variables
    global sol
    global rover
    global cam
    api_key = '&api_key=DEMO_KEY'
    url_root = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'
    date_num= str(sol)
    date ='?sol='+date_num
#    p_num = 0
 #   p = '&page='+str(p_num)
    url = url_root+rover+'/photos'+date+'&camera='+cam+api_key

    #Requisition
    if valid_picks(ev) == True:
        req = ajax.ajax()
        req.open('GET', url, True)
        req.bind('complete', on_complete)
        req.send()

doc['btn'].bind('click', search)

#page flips
#def page_fwd(ev):

#doc['btn_fwd'].bind('click', page_fwd)

#def page_back(ev):

#doc['btn_back'].bind('click', page_back)
