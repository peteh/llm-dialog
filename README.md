# Large Language Model Dialogue

A tool to let LLMs talk to each other and generate a dialogue with Text To Speech. Currently it supports Ollama and PiperTTS or XTTS models via CoqUI TTS.

## Running the Dialogue

First create your virtual env to run the examples in:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`example_piper_en.py`: Uses Piper TTS with English voice models.

`example_piper_de.py`: Uses Piper TTS with German voice models and german prompt.

The output is stored by default in `/output/` and contains a `dialogue.txt` and a `dialogue.wav` which contains the tts generated voices.

## Using higher quality Voice Models

The tool also implements XTTS voice models using CoqUI TTS. To train such a model you can follow this tutorial:

<https://www.youtube.com/watch?v=8tpDiiouGxc>

Store the model files in a separate folde, e.g. named `xtts`:

```bash
/xtts
- vocab.json
- model.pth
- config.json
- reference.wav # refence wav from the training set that sets the tone for the model
```

Then you can create a tts instance:

```python
tts_a = XTTS("xtts", default_lang="en")
```

This tts instance can be passed to the Dialogue Manager as shown in the examples.

## Examples

The following examples are generated text using Llama3 asked to discuss "Banning flights for the environment" with contrary opinions.

### Llama3 and XTTS

>B: Hello
>
>A: Hey Angy! How's it going? I'm Arnold, nice to chat with you about this topic that's been on my mind lately - banning flights for the environment. So, what do you think about it?
>
>B: Hey Arnold! I've gotta be honest, I think we gotta take a stand and ban those flights if we wanna save our planet. Air travel is one of the biggest contributors to greenhouse gas emissions, you know? We can't just keep flying high and hoping for the best. We need some drastic changes, ASAP!
>
>A: I hear you, Angy, but I gotta respectfully disagree. Flights are a huge part of economic growth, especially for developing countries. They connect people, cultures, and businesses. Banning flights would have a devastating impact on those economies. Plus, have you seen the progress being made in sustainable aviation fuels? It's like, we're not giving up yet!
>
>B: Fair point, Arnold! I get that economic growth is important, but let's not forget the bigger picture here – climate change ain't no joke! We can't just keep relying on fossil fuels and hoping for a miracle. Those sustainable aviation fuels are great, don't get me wrong, but they're still gonna be a niche solution at best.
>
>I mean, have you seen those carbon footprint calculators? Even with the most eco-friendly flights, it's still like, woah! We gotta think about our grandkids' future here. I'm not saying we gotta ban flights cold turkey, maybe phase them out gradually and invest in alternative modes of transport. The point is, we can't keep business as usual – it's time for a change!
>
>A: You're preaching to the choir, Angy! I totally get where you're coming from. Climate change is real, and we gotta take action. But, I'm still not convinced that banning flights is the way to go. Like, have you seen the job opportunities in the aviation industry? It's a massive employer! And what about emergency services, like medical transport or disaster relief? We can't just cut off our access to those areas.
>
>And don't get me wrong, I'm all for investing in alternative modes of transport – electric cars, high-speed rail, you name it. But, let's not forget that flights are still a vital part of global connectivity. Maybe we need to find a balance between reducing emissions and preserving the benefits of air travel?
>
>B: Exactly, Arnold! You're speaking my language now! I'm all about finding that balance – it's not an either/or situation.
>
>I get what you mean about job opportunities in the aviation industry – those are important too. And yeah, emergency services like medical transport and disaster relief are super crucial. Maybe we can find ways to make those flights more sustainable, like using electric or hybrid aircraft?
And I'm with you on investing in alternative modes of transport – that's where the future is at! But for now, let's focus on reducing emissions from flights while still allowing them to serve their purpose.
You know what? I think we're onto something here, Arnold. Maybe instead of banning flights altogether, we could implement a ticket surcharge for carbon offsetting or invest in green aviation technologies?
What do you say? You up for exploring some compromise solutions with me?
>
>A: Hell yeah, Angy! I'm all about finding common ground and exploring compromise solutions. A ticket surcharge for carbon offsetting is a great idea - it's like, we're acknowledging the impact of flights on the environment while still allowing people to travel. And investing in green aviation technologies could be game-changer.
>
>You know what? I think we might have stumbled upon something here. Maybe instead of banning flights entirely, we can implement a tiered system where flights are classified based on their environmental impact. Like, short-haul flights or ones with low emissions get a pass, while long-haul or high-emission flights are subject to the ticket surcharge.
>
>And don't even get me started on the potential for electric or hybrid aircraft - that's like, the holy grail of sustainable aviation right there! We could be looking at a future where air travel is not only more accessible but also more environmentally friendly.
>
>You know what I'm saying? This compromise thing might just work out after all.
>
>B: Hell yeah, Arnold! I'm stoked that we're on the same page now! That tiered system idea of yours is pure genius – it's like, acknowledging the nuances of flight emissions and taking steps to mitigate their impact.
And yeah, electric or hybrid aircraft would be a total game-changer! Can you imagine the possibilities? Not only would air travel become more sustainable, but we'd also be paving the way for a cleaner, greener future.
>
>I'm so down with exploring this compromise solution further. It's like, we're not giving up on the environment, but we're also not cutting off our access to global connectivity and economic growth. This is exactly what I mean by "finding common ground" – it's about working together towards a better tomorrow.
>
>Let's keep the conversation going, Arnold! What do you say? You in for a brainstorming session to see how far we can take this compromise solution?
>
>A: Hell yeah, Angy! I'm so down for that brainstorming session! Let's get our thinking caps on and see what kind of innovative solutions we can come up with.
>
>I mean, just think about it - if we can make air travel more sustainable, we're not only reducing emissions but also making the industry more viable in the long run. It's like, a win-win situation!
>
>And yeah, let's not forget about the job opportunities and economic growth that comes with aviation. We can create new industries around sustainable aviation tech, green infrastructure, and eco-friendly tourism. The possibilities are endless!
>
>So, what do you say? You up for a marathon brainstorming session to see where our compromise solution takes us? Let's get creative and make some magic happen!
>
>B: YESSSSSS! I'm SO down for that brainstorming session, Arnold! Let's get this creative party started!
>
>You're absolutely right - making air travel more sustainable is a win-win situation. We can reduce emissions, create new industries, and drive economic growth all at once. It's like, the ultimate triple threat!
>
>Alright, let's get our thinking caps on and start brainstorming some innovative solutions! What do you say we start with? Should we tackle the ticket surcharge, green aviation tech, or maybe eco-friendly tourism? The possibilities are endless, my friend!

Here is the corresponding audio output using higher quality XTTS models:

https://github.com/peteh/llm-dialog/assets/918728/bc4038b0-058b-422f-b169-ef8a3d23d058

### Llama 3 and Piper TTS

>B: Hello
>
>A: Hey Angy! What's up? You're still pushing for banning flights, huh? I gotta respectfully disagree. Flights are a lifeline for economies worldwide. They connect people and cultures, facilitate trade and tourism... and that's just the tip of the iceberg!
>
>B: Come on Arnold! You're not seeing the bigger picture here. Climate change is real, and flights are a major contributor to emissions. Have you seen those graphs showing the exponential rise in CO2 levels? It's like a ticking time bomb! We gotta take drastic measures now to mitigate the damage. Banning flights isn't the answer, but we do need radical changes in aviation industry ASAP!
>
>A: I get where you're coming from, Angy, but let's not forget that planes aren't just about pleasure trips or vacations – they're also a vital means of transportation for people and goods. You can't just ban flights without considering the impact on global supply chains and economies! And yeah, I've seen those graphs too... but what about the alternatives? We need to invest in sustainable aviation fuels, improve aircraft efficiency, and develop green technologies that can be scaled up – not tear down a vital infrastructure like flights.
>
>B: You're right, Arnold, planes are crucial for transporting people and goods. But I still think we're putting too much faith in the idea that technology will magically solve this problem. I mean, have you seen the timeline for when these sustainable fuels and green tech solutions will be widely available? It's years, maybe even decades away! In the meantime, emissions are only going to continue rising. We need to take bold action now to make a difference. And what about all the carbon offsets and "green" flights that are just Band-Aids on a bullet wound? Let's not get distracted by false solutions when we should be focusing on systemic change!
>
>A: Angy, I hear you, but let's not throw the baby out with the bathwater! Technology is advancing faster than ever before – and yes, it'll take time to scale up sustainable fuels and green tech. But that doesn't mean we should abandon flights altogether! We need to work together to create a roadmap for transition, investing in R&D and implementing incremental changes that make a real difference. Carbon offsets might not be perfect, but they're a step towards accounting for emissions – and who's to say that innovative solutions won't emerge from the private sector or academia? We can't just give up on progress because we haven't found the holy grail of sustainable aviation yet!


And here the output using PiperTTS

https://github.com/peteh/llm-dialog/assets/918728/cfd12a9e-a82e-453a-a209-8ca4506dd8b2

## Credits

Ollama \
<https://github.com/ollama/ollama>

PiperTTS \
<https://github.com/rhasspy/piper>

CoqUI TTS \
<https://github.com/coqui-ai/TTS>

