import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
Extra_bilgiler = [
 "1.Plastik Tüketimini Azaltmak: Plastik atıklar, çevre kirliliğinin en büyük kaynaklarından biridir. Dünya genelinde her yıl milyonlarca ton plastik üretilmekte ve büyük bir kısmı doğrudan denizlere, okyanuslara ulaşmaktadır. Plastik tüketimini azaltmak için şu adımlar atılabilir:Tek kullanımlık plastik ürünlerden (plastik şişeler, pipetler, poşetler) kaçınarak, yeniden kullanılabilir alternatifler kullanabilirsiniz.Alışverişte kumaş torbalar ve bez çantalar tercih ederek plastik poşet kullanımını azaltabilirsiniz.Plastik ambalajdan kaçınan markaları destekleyebilir ve toplu ürün alarak ambalaj atıklarını azaltabilirsiniz." 
,"2.Su Tasarrufu: Su kaynakları hızla tükenmektedir ve su tasarrufu yapmak, sürdürülebilir bir yaşam için önemlidir. Su tasarrufu için şu yöntemler kullanılabilir: Düşük akışlı duş başlıkları ve musluklar kullanarak su tüketimini azaltabilirsiniz. Bahçenizi sularken sabah erken saatlerde veya akşam geç saatlerde sulama yaparak suyun buharlaşmasını önleyebilirsiniz. Tuvaletlerde su tasarrufu sağlayan çift kademeli sifonlar kullanarak su kullanımını minimize edebilirsiniz."
,"3.Geri Dönüşümün Önemi: Geri dönüşüm, atıkların tekrar işlenerek yeniden kullanılmasını sağlar ve doğal kaynakların korunmasına yardımcı olur. Geri dönüşümün çevreye olan olumlu etkileri şunlardır:Geri dönüştürülen malzemeler, yeni ürünler üretmek için ham madde olarak kullanıldığında, enerji tüketimi ve karbon salınımı önemli ölçüde azalır. Kağıt geri dönüşümü, ormanların korunmasına katkı sağlar ve ağaç kesimini azaltır. Metal geri dönüşümü, madencilik faaliyetlerini ve buna bağlı olarak çevre tahribatını azaltır. Bu bilgiler, çevre dostu uygulamalar ve atıkları azaltma konularında farkındalık yaratmak ve sürdürülebilir bir yaşam tarzına katkıda bulunmak için önemlidir."
    
]


@bot.command()
async def Extra_bilgi(ctx):
    await ctx.send("1. Atıkları Azaltma Yöntemleri Geri Dönüşüm: Plastik, cam, kağıt, metal gibi materyalleri geri dönüşüm kutularına atarak doğal kaynakları koruyabilirsiniz.Kompostlama: Organik atıkları (gıda artıkları, bitki atıkları) kompost yaparak toprağın verimliliğini artırabilirsiniz.Azaltma ve Yeniden Kullanma: Tek kullanımlık ürünlerden kaçınarak, yeniden kullanılabilir ürünler (su şişeleri, kahve fincanları, alışveriş torbaları) tercih edebilirsiniz.Gıda İsrafını Önleme: Planlı alışveriş yaparak, yiyeceklerinizi doğru şekilde saklayarak ve kalan yemekleri değerlendirecek tarifler uygulayarak gıda israfını azaltabilirsiniz.2. Enerji VerimliliğiEnerji Tasarruflu Cihazlar: Enerji tasarruflu beyaz eşyalar ve LED ampuller kullanarak enerji tüketimini azaltabilirsiniz.Yalıtım: Evinizi iyi yalıtarak kışın ısınma, yazın soğutma masraflarını ve enerji tüketimini azaltabilirsiniz.Yenilenebilir Enerji: Güneş panelleri veya rüzgar türbinleri gibi yenilenebilir enerji kaynaklarını kullanarak fosil yakıt tüketimini azaltabilirsiniz.")

@bot.command()
async def Rastgele_bilgi(ctx):
    await ctx.send(random.choice(Extra_bilgiler))

bot.run("token")
