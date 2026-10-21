import json,os,re
from PIL import Image
os.makedirs('assets/images',exist_ok=True);os.makedirs('assets/css',exist_ok=True);os.makedirs('assets/js',exist_ok=True)
im=Image.open('/mnt/user-data/uploads/314526.png').convert('RGB')
im.resize((640,640)).save('assets/images/logo.png',optimize=True)
im.crop((60,60,1190,1190)).resize((64,64)).save('assets/images/favicon.png')
im.resize((1200,1200)).save('assets/images/og.jpg',quality=80)
C=[("A","Organic & Natural Products","organic-natural","#5f7f3a","🌿","Natural product",
"Natural Raw Honey,Wildflower Honey,Sidr Honey,Acacia Honey,Organic Dates,Natural Dried Figs,Dried Apricots,Natural Raisins,Raw Almonds,Natural Walnuts,Pumpkin Seeds,Sunflower Seeds,Chia Seeds,Flax Seeds,Natural Sesame Seeds,Dried Mint,Dried Rosemary,Dried Thyme,Natural Turmeric Powder,Natural Ginger Powder,Cinnamon Sticks,Black Peppercorns,Natural Cumin Seeds,Dried Chamomile Flowers,Natural Herbal Tea Blend","250 g"),
("B","Natural & Botanical Oils","natural-oils","#b8892b","🧴","Cosmetic / botanical oil (not for eating)",
"Sweet Almond Oil,Coconut Oil,Jojoba Oil,Argan Oil,Castor Oil,Olive Cosmetic Oil,Rosemary Essential Oil,Lavender Essential Oil,Tea Tree Essential Oil,Peppermint Essential Oil,Eucalyptus Essential Oil,Lemongrass Essential Oil,Black Seed Oil,Kalonji Oil,Mustard Massage Oil,Sesame Body Oil,Avocado Oil,Grapeseed Oil,Neem Oil,Amla Hair Oil,Bhringraj Hair Oil,Herbal Hair Oil Blend,Beard Care Oil,Botanical Massage Oil,Natural Cuticle Oil","100 ml"),
("C","Edible & Cooking Oils","edible-oils","#c9a227","🫒","Edible oil (food use)",
"Extra Virgin Olive Oil,Pure Olive Oil,Coconut Cooking Oil,Mustard Cooking Oil,Sesame Cooking Oil,Sunflower Oil,Canola Oil,Rice Bran Oil,Peanut Oil,Avocado Cooking Oil,Walnut Oil,Flaxseed Oil,Pumpkin Seed Oil,Grapeseed Cooking Oil,Cold-Pressed Sesame Oil,Cold-Pressed Mustard Oil,Cold-Pressed Coconut Oil,Cold-Pressed Groundnut Oil,Cold-Pressed Sunflower Oil,Cold-Pressed Flaxseed Oil,Cooking Oil Gift Set,Olive Oil Sample Bottle,Premium Cooking Oil Collection,Traditional Mustard Oil Bottle,Everyday Cooking Oil Collection","500 ml"),
("D","Honey Collection","honey","#d98a1b","🍯","Honey",
"Sidr Honey,Acacia Honey,Wildflower Honey,Multifloral Honey,Clover Honey,Citrus Blossom Honey,Mountain Flower Honey,Forest Honey,Raw Honey,Comb Honey,Honeycomb Pieces,Creamed Honey,Ginger-Infused Honey,Cinnamon-Infused Honey,Lemon-Infused Honey,Honey Squeeze Bottle,Honey Glass Jar,Family Honey Jar,Premium Honey Gift Box,Honey Tasting Collection,Mini Honey Jar Set,Honey and Wooden Dipper Set,Breakfast Honey Collection,Honey Gift Hamper,Everyday Honey Jar","500 g"),
("E","Dry Fruits & Nuts","dry-fruits","#8a5a35","🥜","Dry fruit / nut",
"Premium Almonds,Whole Cashews,Pistachios,Walnut Kernels,Premium Dates,Ajwa Dates,Medjool Dates,Dried Figs,Golden Raisins,Black Raisins,Dried Apricots,Dried Cranberries,Dried Blueberries,Dried Mango,Dried Pineapple,Hazelnuts,Pecans,Brazil Nuts,Macadamia Nuts,Pine Nuts,Roasted Almonds,Roasted Cashews,Mixed Nuts,Premium Trail Mix,Dry Fruit Gift Box","250 g"),
("F","Seeds, Grains & Pantry","seeds-grains","#7d8f4a","🌾","Pantry staple",
"Chia Seeds,Flax Seeds,Pumpkin Seeds,Sunflower Seeds,Sesame Seeds,Basil Seeds,Watermelon Seeds,Melon Seeds,Psyllium Husk,Quinoa,Oats,Brown Rice,Millet,Buckwheat,Barley,Chickpeas,Red Lentils,Green Lentils,Mung Beans,Natural Pantry Essentials Box","500 g"),
("G","Spices & Herbs","spices-herbs","#a8432b","🌶️","Spice / herb",
"Turmeric Powder,Ginger Powder,Cinnamon Powder,Whole Cinnamon,Black Pepper,White Pepper,Green Cardamom,Black Cardamom,Cloves,Cumin Seeds,Coriander Seeds,Fennel Seeds,Fenugreek Seeds,Carom Seeds,Nigella Seeds,Dried Mint,Dried Rosemary,Dried Oregano,Herbal Tea Blend,Premium Spice Gift Box","100 g"),
("H","Natural Personal Care","personal-care","#b86f8a","🌸","Cosmetic product",
"Natural Aloe Vera Gel,Rose Water,Orange Blossom Water,Shea Butter,Cocoa Butter,Natural Lip Balm,Botanical Body Butter,Natural Body Lotion,Herbal Shampoo,Botanical Conditioner,Gentle Facial Cleanser,Clay Face Mask,Natural Bath Salts,Botanical Soap Bar,Handmade Soap Collection,Herbal Hair Mask,Natural Foot Balm,Body Massage Balm,Botanical Skin Care Gift Set,Personal Care Starter Kit","150 ml"),
("I","Premium Special Collections","special-collections","#123D2B","🎁","Gift collection",
"Punjab Naturals Signature Gift Box,Honey Lover's Gift Box,Premium Dry Fruit Hamper,Natural Oils Discovery Set,Cooking Oils Selection Box,Botanical Self-Care Hamper,Natural Pantry Gift Set,Premium Dates Collection,Nuts and Seeds Gift Box,Honey and Dry Fruits Hamper,Essential Oils Starter Set,Herbal Tea Gift Set,Family Wellness Basket,Traditional Kitchen Essentials,Premium Spice Collection,Seasonal Gift Hamper,Corporate Gift Box,Celebration Gift Basket,Premium Natural Products Box,Punjab Naturals Signature Collection","1 set")]
SAFE={"A":"Store in a cool, dry place in an airtight container. Check ingredients and allergens on the final supplier label.",
"B":"For external cosmetic use only; not for eating. Patch-test first. Essential oils must be diluted in a carrier oil before skin use and kept away from children and pets. No medical claims are made.",
"C":"For food use. Store sealed, away from heat and light. Cold-pressed/pure status shown only once the supplier confirms it.",
"D":"Store at room temperature, sealed. Do not give honey to infants under 12 months. Raw/infused/comb status per supplier specification.",
"E":"May contain or be processed with nuts, peanuts or sesame. Store airtight in a cool, dry place.",
"F":"Store airtight in a dry place. Check allergens on the supplier label.",
"G":"Store airtight away from moisture and sunlight. Check allergens on the supplier label.",
"H":"Cosmetic product for external use. Patch-test first. Stop use if irritation occurs. No treatment claims are made.",
"I":"Contents and allergens depend on the final packed items; confirm with our team before ordering."}
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
P=[];seen=set()
for c in C:
  for i,n in enumerate(c[6].split(',')):
    s=slug(n)
    if s in seen:s=s+'-'+c[2]
    seen.add(s)
    pr=250+((i*137+ord(c[0])*31)%40)*25
    P.append(dict(id=f"PN-{c[0]}{i+1:03d}",slug=s,name=n,cat=c[0],
     desc=f"{n} in the Punjab Naturals {c[1].lower()} range: a proposed catalog listing. Final specifications, sourcing and packaging will be confirmed with supplier details.",
     unit=c[7],price=pr,priceStatus="demo",availability="Availability to be confirmed",
     type=c[5],featured=(i%7==0),isNew=(i%11==3),premium=(c[0]=="I"),
     specs=dict(Type=c[5],Origin="To be confirmed",Ingredients="To be confirmed by supplier"),safety=SAFE[c[0]],
     metaTitle=f"{n} | Punjab Naturals Pakistan",metaDesc=f"View {n} from Punjab Naturals ({c[1]}). Demo listing; confirm price, stock and delivery on WhatsApp."))
assert len(P)==205 and len({p['id'] for p in P})==205
cats=[dict(id=c[0],name=c[1],slug=c[2],color=c[3],icon=c[4]) for c in C]
open('assets/js/products.js','w').write("// CENTRAL CATALOG: edit prices, units, availability here. priceStatus 'demo' -> 'confirmed' once real.\nconst CATEGORIES="+json.dumps(cats,ensure_ascii=False)+";\nconst PRODUCTS="+json.dumps(P,ensure_ascii=False,separators=(',',':'))+";\n")
D=CFG="https://YOUR-USERNAME.github.io/REPO"
def page(path,title,desc,page,body="",extra=""):
  d=path.count('/');R='../'*d
  h=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{D}/{path}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{D}/assets/images/og.jpg"><meta name="theme-color" content="#123D2B"><link rel="icon" href="{R}assets/images/favicon.png"><link rel="stylesheet" href="{R}assets/css/style.css">{extra}</head><body data-page="{page}" data-root="{R}"><div id="hdr"></div><main id="app">{body}</main><div id="ftr"></div><script src="{R}assets/js/config.js"></script><script src="{R}assets/js/products.js"></script><script src="{R}assets/js/app.js"></script></body></html>'''
  os.makedirs(os.path.dirname(path) or '.',exist_ok=True);open(path,'w').write(h)
urls=[]
def add(*a,**k):page(*a,**k);urls.append(a[0])
add('index.html',"Punjab Naturals | Honey, Natural Oils & Dry Fruits in Pakistan","Explore Punjab Naturals for honey, natural oils, edible oils, dry fruits, herbs, spices, and thoughtfully selected natural essentials. Discover our collections and order conveniently through WhatsApp.","home")
add('shop.html',"Shop All Natural Products | Punjab Naturals","Browse the Punjab Naturals demo catalog: honey, oils, dry fruits, spices, personal care and gift collections.","shop")
add('category.html',"Categories | Punjab Naturals","Browse Punjab Naturals categories.","shop")
add('product.html',"Product | Punjab Naturals","Product details","product")
for c in cats:
  add(f"category/{c['slug']}.html",f"{c['name']} | Punjab Naturals",f"Browse {c['name']} from Punjab Naturals. Demo listings; confirm price and stock on WhatsApp.","shop").__class__
  s=open(f"category/{c['slug']}.html").read().replace('data-page="shop"',f'data-page="shop" data-cat="{c["id"]}"');open(f"category/{c['slug']}.html",'w').write(s)
for p in P:
  add(f"product/{p['slug']}.html",p['metaTitle'],p['metaDesc'],"product");s=open(f"product/{p['slug']}.html").read().replace('data-page="product"',f'data-page="product" data-id="{p["id"]}"');open(f"product/{p['slug']}.html",'w').write(s)
add('about.html',"About Punjab Naturals | Rooted in Nature. Guided by Trust.","About Punjab Naturals: honest, transparent natural products.","about")
add('contact.html',"Contact Punjab Naturals | WhatsApp & Email","Contact Punjab Naturals via WhatsApp or email.","contact")
for n,t in [("privacy-policy","Privacy Policy"),("terms","Terms and Conditions"),("shipping-policy","Delivery and Shipping Policy"),("returns-policy","Returns and Refunds Policy"),("faq","Frequently Asked Questions")]:
  add(n+'.html',t+" | Punjab Naturals",t+" for Punjab Naturals (draft, to be finalised by the owner).","policy",f"<section class='wrap pol'><h1>{t}</h1><p>DRAFT: replace with your confirmed policy. Orders are placed via WhatsApp and are not confirmed until our team confirms availability, delivery charges and the total payable amount.</p></section>")
page('404.html',"Page not found | Punjab Naturals","Page not found","policy","<section class='wrap pol'><h1>Page not found</h1><p><a href='/'>Return home</a> or <a href='shop.html'>shop all products</a>.</p></section>")
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{D}/{u}</loc></url>' for u in urls)+'</urlset>')
open('robots.txt','w').write(f"User-agent: *\nAllow: /\nSitemap: {D}/sitemap.xml\n")
print(len(P),len(urls))
