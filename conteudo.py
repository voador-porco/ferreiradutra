"""Textos do site da Ferreira e Dutra Advogados (o build.py importa daqui).

Esquema (o build depende destes nomes e formatos exatos):

ESCRITORIO = {
    "hero_h1": str,              # até 42 caracteres, fecha em 2 linhas no celular
    "hero_p": str,               # 1 ou 2 frases
    "seletor_h": str,            # pergunta curta acima dos atalhos de situação na capa (até 34 caracteres)
    "sobre_h2": str,
    "sobre": [str, str],         # 2 parágrafos curtos
    "manifesto": str,            # 35 a 55 palavras, lido palavra a palavra na rolagem
    "diferenciais": [(titulo, texto)] * 5,   # experiência, comprometimento, dedicação, estudo constante, técnica
    "areas_h2": str,
    "como_h2": str,
    "como": [(titulo, texto)] * 4,           # do primeiro contato ao acompanhamento
    "alcance_h2": str, "alcance_p": str,     # Uberlândia e todo o Brasil por processo eletrônico
    "faq": [(pergunta, resposta)] * 6,
    "final_h2": str, "final_p": str,
}

AREAS = [  # nesta ordem: criminal, inventario, familia, civel, transito, administrativo
    {
        "slug": str, "nome": str, "curto": str,
        "gatilho": str,          # atalho da capa, na voz do cliente, até 34 caracteres
        "card": str,             # 1 frase para o índice de áreas da página central
        "seo_titulo": str,       # até 60 caracteres, com Uberlândia
        "seo_descricao": str,    # até 155 caracteres
        "hero_h1": str,          # até 44 caracteres
        "hero_p": str,
        "cta": str,              # rótulo do botão, até 26 caracteres
        "msg": str,              # mensagem que já vai escrita no WhatsApp
        "situacoes_h2": str, "situacoes": [(titulo, texto)] * 6,
        "atuacao_h2": str, "atuacao": [(titulo, texto)] * 4,
        "documentos_h2": str, "documentos": [str] * 5 a 8,   # ou "" e [] quando não fizer sentido
        "faq": [(pergunta, resposta)] * 5,
        "final_h2": str,
    },
]
"""

ESCRITORIO = {
    "hero_h1": "Advocacia criminal, de família e cível",
    "hero_p": (
        "Você conta o que está acontecendo, nós estudamos o caso e conduzimos "
        "cada etapa com você. Em Uberlândia e, por processo eletrônico, em "
        "qualquer lugar do Brasil."
    ),
    "seletor_h": "Qual destas é a sua situação?",
    "sobre_h2": "Quem cuida do seu caso",
    "sobre": [
        "A Ferreira e Dutra Advogados é um escritório de Uberlândia com dois "
        "sócios, um advogado e uma advogada. A área criminal é o centro do "
        "nosso trabalho, ao lado de família e sucessões e do direito cível.",
        "Trabalhamos para solucionar problemas jurídicos: uma prisão, um "
        "inventário, um divórcio, a defesa em um processo. Você entende o que "
        "está acontecendo no seu caso, explicado em palavras simples, sem "
        "juridiquês.",
    ],
    "manifesto": (
        "Ninguém procura um advogado num dia comum. Procura quando alguém foi "
        "preso, quando a família perdeu uma pessoa, quando um casamento acabou "
        "ou quando chegou um processo. Nesse momento, você precisa de alguém "
        "que estude o caso a fundo, fale claro e seja honesto sobre o que pode "
        "ser feito. É assim que trabalhamos."
    ),
    "diferenciais": [
        (
            "Experiência",
            "A prática nas áreas criminal, de família e cível ajuda a enxergar "
            "os próximos passos do processo e a preparar você para cada um deles.",
        ),
        (
            "Comprometimento",
            "Quando assumimos um caso, você sabe o que está sendo feito e por "
            "quê. Cada passo é explicado em palavras simples.",
        ),
        (
            "Dedicação",
            "Cada caso é estudado de perto: o processo inteiro, cada documento e "
            "cada prova são lidos antes de decidir o próximo passo.",
        ),
        (
            "Estudo constante",
            "A lei muda e o entendimento dos tribunais também. Acompanhamos essas "
            "mudanças para que a sua defesa use o que vale hoje.",
        ),
        (
            "Técnica",
            "Cada peça é escrita para o seu caso, com base na lei e nas decisões "
            "dos tribunais, sem modelo pronto.",
        ),
    ],
    "areas_h2": "Em quais casos o escritório atua",
    "como_h2": "Como o seu caso é conduzido",
    "como": [
        (
            "Você conta o que aconteceu",
            "Por mensagem ou em uma conversa marcada, você explica a situação. "
            "Entendemos o que é urgente e se é um caso que o escritório atende.",
        ),
        (
            "Proposta por escrito",
            "Explicamos como vamos atuar e quais são os honorários. Tudo fica em "
            "contrato, assinado antes de o trabalho começar.",
        ),
        (
            "Estudo e atuação",
            "Com o contrato assinado, estudamos o caso a fundo e tomamos as "
            "providências, começando pelas mais urgentes.",
        ),
        (
            "Acompanhamento",
            "Você é informado de cada movimentação importante, explicada em "
            "palavras simples, até o encerramento do caso.",
        ),
    ],
    "alcance_h2": "De Uberlândia para todo o Brasil",
    "alcance_p": (
        "Atendemos em Uberlândia e, quando o caso pede, em outras cidades e "
        "estados. Com o processo eletrônico, o trabalho no processo e a conversa "
        "com você podem ser feitos a distância."
    ),
    "faq": [
        (
            "Vocês atendem fora de Uberlândia?",
            "Sim. Quando o processo é eletrônico, atuamos em qualquer lugar do "
            "Brasil, e a conversa com você pode ser toda a distância. Se algum "
            "ato exigir presença, avisamos antes de começar.",
        ),
        (
            "Como são combinados os honorários?",
            "Depois de entender o seu caso, apresentamos a proposta de honorários "
            "por escrito. Tudo fica em contrato, assinado antes de o trabalho "
            "começar.",
        ),
        (
            "Vocês prometem resultado?",
            "Não. Quem decide é o juiz ou o órgão responsável, e a ética da "
            "advocacia proíbe prometer resultado. O nosso compromisso é com o "
            "trabalho: estudo do caso, técnica e acompanhamento em cada etapa.",
        ),
        (
            "Alguém da minha família foi preso. O que eu faço?",
            "Fale com o escritório o quanto antes, com o nome completo da pessoa "
            "e o local onde ela está. A defesa começa na audiência de custódia, "
            "quando o juiz decide se a prisão continua.",
        ),
        (
            "O que eu conto fica em sigilo?",
            "Sim. O sigilo entre advogado e cliente é um dever profissional. O "
            "que você conta fica entre você e o escritório.",
        ),
        (
            "O que levar para a primeira conversa?",
            "Um resumo do que aconteceu e os documentos que você tiver. Na página "
            "de cada área há uma lista do que separar.",
        ),
    ],
    "final_h2": "Conte o que está acontecendo",
    "final_p": (
        "Mande uma mensagem com um resumo da situação e retornamos para entender "
        "o seu caso. Em caso de prisão, fale com o escritório o quanto antes."
    ),
}

AREAS = [
    # 1. CRIMINAL ------------------------------------------------------------
    {
        "slug": "criminal",
        "nome": "Direito Criminal",
        "curto": "Criminal",
        "gatilho": "Alguém da família foi preso",
        "card": (
            "Defesa desde a prisão em flagrante até o júri, os recursos e o "
            "cumprimento da pena."
        ),
        "seo_titulo": "Advogado criminalista em Uberlândia | Ferreira e Dutra",
        "seo_descricao": (
            "Defesa criminal em Uberlândia: prisão em flagrante, audiência de "
            "custódia, inquérito, processo, júri, recursos e execução penal. "
            "Fale com o escritório."
        ),
        "hero_h1": "Defesa criminal desde a prisão em flagrante",
        "hero_p": (
            "Se alguém da sua família foi preso, fale com o escritório o quanto "
            "antes. A defesa começa na audiência de custódia, quando o juiz "
            "decide se a prisão continua, e segue até o fim do processo."
        ),
        "cta": "Falar com o escritório",
        "msg": "Olá, um familiar foi preso e preciso de ajuda.",
        "situacoes_h2": "Da prisão ao cumprimento da pena",
        "situacoes": [
            (
                "Meu familiar foi preso em flagrante",
                "Verificamos se a prisão seguiu a lei e fazemos a defesa na "
                "audiência de custódia, em que o juiz decide se a pessoa responde "
                "ao processo presa ou em liberdade.",
            ),
            (
                "O juiz manteve a prisão",
                "Quando a prisão vira preventiva, que é a prisão antes do "
                "julgamento, analisamos a decisão e pedimos a liberdade ao juiz "
                "ou ao tribunal sempre que houver fundamento.",
            ),
            (
                "Fui intimado a depor na delegacia",
                "Acompanhamos você no depoimento e durante o inquérito, que é a "
                "investigação feita pela polícia antes de existir um processo.",
            ),
            (
                "Estou respondendo a um processo criminal",
                "Lemos a acusação e as provas, apresentamos a defesa por escrito "
                "e acompanhamos cada audiência até a sentença.",
            ),
            (
                "O caso vai para o júri popular",
                "Crimes contra a vida são julgados por jurados, cidadãos da "
                "comunidade. Preparamos a defesa em todas as fases, até o dia do "
                "julgamento.",
            ),
            (
                "Já saiu a condenação",
                "Avaliamos se cabe recurso ao tribunal. Durante o cumprimento da "
                "pena, pedimos os direitos previstos em lei, como a passagem para "
                "um regime mais brando.",
            ),
        ],
        "atuacao_h2": "Como conduzimos a defesa",
        "atuacao": [
            (
                "Primeiro contato",
                "Você nos passa o nome completo da pessoa, onde ela está e o que "
                "se sabe do caso. Com isso, vemos o que precisa ser feito primeiro.",
            ),
            (
                "Contrato e início",
                "Combinamos os honorários por escrito e começamos. Em caso de "
                "prisão, o trabalho começa pelas medidas mais urgentes.",
            ),
            (
                "Estudo do caso",
                "Lemos o inquérito ou o processo inteiro, as provas e os "
                "depoimentos, e montamos a linha da defesa.",
            ),
            (
                "Defesa e acompanhamento",
                "Atuamos em cada audiência, prazo e recurso. A família recebe "
                "notícias do andamento, explicadas em palavras simples.",
            ),
        ],
        "documentos_h2": "O que informar no primeiro contato",
        "documentos": [
            "Nome completo e data de nascimento da pessoa presa ou investigada",
            "Onde ela está agora: delegacia, presídio ou outra cidade",
            "Data, horário e local da prisão",
            "O que se sabe sobre o motivo da prisão ou da investigação",
            "Número do boletim de ocorrência, do inquérito ou do processo, se você tiver",
            "Papéis entregues pela polícia ou pela Justiça, como mandado ou intimação",
            "Seu nome, seu telefone e sua relação com a pessoa",
        ],
        "faq": [
            (
                "O que é a audiência de custódia?",
                "É a audiência feita logo depois da prisão em flagrante. Nela, o "
                "juiz verifica se a prisão foi legal e decide se a pessoa responde "
                "ao processo presa ou em liberdade. A lei prevê que ela aconteça "
                "em até 24 horas.",
            ),
            (
                "Vocês podem prometer a liberdade?",
                "Não. Quem decide é o juiz, e a ética da advocacia proíbe prometer "
                "resultado. O que fazemos é verificar se a prisão seguiu a lei e "
                "pedir a liberdade sempre que houver fundamento.",
            ),
            (
                "A família pode contratar o advogado?",
                "Sim. Em casos de prisão, é comum que um familiar faça o primeiro "
                "contato e assine o contrato. A defesa é da pessoa presa, e o que "
                "ela conta ao advogado fica em sigilo.",
            ),
            (
                "O caso é em outra cidade. Vocês atuam?",
                "Sim. Quando o processo é eletrônico, atuamos em qualquer lugar do "
                "Brasil e falamos com a família a distância. Se algum ato exigir "
                "presença, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato diz quais fases estão incluídas, como inquérito, "
                "processo, júri ou recurso, e o trabalho começa com ele assinado.",
            ),
        ],
        "final_h2": "Houve prisão? Fale conosco o quanto antes",
    },
    # 2. INVENTÁRIO ----------------------------------------------------------
    {
        "slug": "inventario",
        "nome": "Inventário e Sucessões",
        "curto": "Inventário",
        "gatilho": "Preciso fazer um inventário",
        "card": (
            "Inventário em cartório ou na Justiça, partilha de bens e testamento, "
            "também quando a família não se entende."
        ),
        "seo_titulo": "Advogado de inventário em Uberlândia | Ferreira e Dutra",
        "seo_descricao": (
            "Inventário em cartório ou judicial, partilha de bens e testamento em "
            "Uberlândia, também quando os herdeiros não estão de acordo. Fale com "
            "o escritório."
        ),
        "hero_h1": "Inventário em cartório ou na Justiça",
        "hero_p": (
            "Cuidamos do inventário e da partilha, que é a divisão dos bens de quem "
            "faleceu, com ou sem acordo entre os herdeiros. A família entende cada "
            "etapa e sabe o que falta para terminar."
        ),
        "cta": "Falar sobre o inventário",
        "msg": "Olá, preciso de ajuda com um inventário.",
        "situacoes_h2": "Quando a família precisa dividir os bens",
        "situacoes": [
            (
                "Um familiar faleceu e deixou bens",
                "Levantamos quem são os herdeiros e quais bens existem, e indicamos "
                "o caminho possível: inventário em cartório ou na Justiça.",
            ),
            (
                "Os herdeiros estão de acordo",
                "Com acordo, em muitos casos o inventário pode ser feito em "
                "cartório, por escritura, sem processo na Justiça. Conduzimos tudo "
                "até a divisão dos bens.",
            ),
            (
                "A família não se entende sobre a divisão",
                "Sem acordo, o inventário vai para a Justiça. Representamos você no "
                "processo e defendemos a sua parte na herança, abrindo espaço para "
                "acordo quando ele for possível.",
            ),
            (
                "O inventário nunca foi aberto",
                "Abrimos inventários atrasados, mesmo de muitos anos atrás. O "
                "atraso pode gerar multa no imposto sobre a herança, então vale "
                "resolver logo.",
            ),
            (
                "Preciso vender um bem de quem faleceu",
                "Em regra, um bem que ainda está no nome de quem faleceu só pode "
                "ser vendido com autorização do juiz, chamada alvará, ou depois da "
                "partilha. Cuidamos desse pedido.",
            ),
            (
                "Quero fazer um testamento",
                "Ajudamos você a fazer o testamento dentro da lei, deixando claro "
                "como os bens serão divididos e reduzindo dúvidas para a família "
                "no futuro.",
            ),
        ],
        "atuacao_h2": "Como cuidamos do inventário",
        "atuacao": [
            (
                "Primeira conversa",
                "Você conta quem faleceu, quem são os herdeiros e quais bens "
                "existem. Com isso, vemos se o caminho é o cartório ou a Justiça.",
            ),
            (
                "Proposta e contrato",
                "Apresentamos os honorários e o que está incluído no trabalho. Tudo "
                "fica em contrato escrito, assinado antes de começar.",
            ),
            (
                "Documentos e imposto",
                "Reunimos certidões e documentos dos bens e cuidamos da declaração "
                "do ITCMD, o imposto sobre a herança, necessário para concluir o "
                "inventário.",
            ),
            (
                "Até a partilha",
                "Acompanhamos a escritura no cartório ou o processo na Justiça até "
                "a divisão dos bens, com a família informada em cada etapa.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "Certidão de óbito",
            "RG e CPF de quem faleceu e de cada herdeiro",
            "Certidão de casamento ou documento de união estável de quem faleceu",
            "Certidões de nascimento ou de casamento dos herdeiros",
            "Matrícula atualizada dos imóveis, que é o registro do imóvel no cartório",
            "Documentos de veículos e extratos de contas e investimentos",
            "Testamento, se existir",
            "Lista das dívidas deixadas, se houver",
        ],
        "faq": [
            (
                "Qual a diferença entre inventário em cartório e na Justiça?",
                "No cartório, o inventário é feito por escritura, quando os "
                "herdeiros estão de acordo e a lei permite. Na Justiça, ele vira um "
                "processo, necessário quando não há acordo ou em outras situações "
                "previstas em lei. Nos dois casos, é obrigatório ter advogado.",
            ),
            (
                "Existe prazo para abrir o inventário?",
                "A lei prevê a abertura em até 2 meses depois do falecimento. "
                "Depois disso o inventário ainda pode ser feito, mas o estado pode "
                "cobrar multa sobre o imposto.",
            ),
            (
                "O que é arrolamento?",
                "É uma forma mais simples de inventário na Justiça, usada quando "
                "todos os herdeiros estão de acordo ou quando o valor dos bens fica "
                "dentro do limite previsto em lei.",
            ),
            (
                "Os herdeiros moram em cidades diferentes. Dá para fazer?",
                "Sim. Conversamos com cada herdeiro a distância e, quando o "
                "processo é eletrônico, atuamos em qualquer lugar do Brasil. Em "
                "cartório, muitas escrituras também podem ser assinadas de forma "
                "eletrônica.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de conhecer os bens e a situação da família, apresentamos a "
                "proposta por escrito. O contrato diz o que está incluído, para "
                "ninguém ter surpresa no meio do caminho.",
            ),
        ],
        "final_h2": "O inventário pode começar por uma mensagem",
    },
    # 3. FAMÍLIA -------------------------------------------------------------
    {
        "slug": "familia",
        "nome": "Direito de Família",
        "curto": "Família",
        "gatilho": "Quero me divorciar ou pedir pensão",
        "card": (
            "Divórcio, pensão alimentícia, guarda e convivência com os filhos e "
            "adoção de criança e adolescente."
        ),
        "seo_titulo": "Advogado de família em Uberlândia | Ferreira e Dutra",
        "seo_descricao": (
            "Divórcio, pensão alimentícia (pedir, revisar ou cobrar), guarda, "
            "convivência e adoção em Uberlândia, com atenção e sigilo. Fale com o "
            "escritório."
        ),
        "hero_h1": "Divórcio, pensão, guarda e adoção",
        "hero_p": (
            "Cuidamos de divórcio com ou sem acordo, pensão para pedir, revisar ou "
            "cobrar, guarda dos filhos e adoção. Você entende cada passo antes de "
            "decidir."
        ),
        "cta": "Conversar sobre o meu caso",
        "msg": "Olá, preciso de ajuda com divórcio, pensão ou guarda.",
        "situacoes_h2": "Quando a vida em família muda",
        "situacoes": [
            (
                "Quero me divorciar",
                "Com acordo, muitas vezes o divórcio pode ser feito em cartório. "
                "Sem acordo, conduzimos o processo na Justiça, incluindo a divisão "
                "dos bens.",
            ),
            (
                "Preciso pedir pensão para meu filho",
                "Pedimos os alimentos, nome que a lei dá à pensão, com base no que "
                "a criança precisa e no que o outro pode pagar. Na gravidez, "
                "também é possível pedir os alimentos gravídicos, a pensão durante "
                "a gestação.",
            ),
            (
                "O valor da pensão precisa mudar",
                "Se a renda de quem paga caiu ou a necessidade de quem recebe "
                "mudou, pedimos a revisão na Justiça. Até o juiz decidir, o valor "
                "atual continua valendo.",
            ),
            (
                "A pensão está atrasada",
                "Cobramos os valores em atraso na Justiça. A lei permite bloquear "
                "contas e bens de quem deve e, em alguns casos, pedir a prisão "
                "civil do devedor.",
            ),
            (
                "Preciso definir a guarda dos meus filhos",
                "Definimos a guarda e os dias de convivência com cada um dos pais, "
                "por acordo ou na Justiça, tendo como centro o interesse da "
                "criança.",
            ),
            (
                "Quero adotar uma criança",
                "Acompanhamos a adoção de criança e adolescente na Vara da "
                "Infância, do cadastro de quem quer adotar até a decisão do juiz. "
                "Também atuamos quando o padrasto ou a madrasta quer adotar o "
                "enteado.",
            ),
        ],
        "atuacao_h2": "Como conduzimos o seu caso de família",
        "atuacao": [
            (
                "Escuta",
                "Você conta o que está acontecendo, no seu tempo. Identificamos o "
                "que é urgente, como a pensão dos filhos, e o que pode esperar.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar.",
            ),
            (
                "Acordo ou processo",
                "Avaliamos com você se há espaço para acordo, que tende a ser mais "
                "rápido e menos desgastante. Se não houver, entramos com o pedido "
                "na Justiça.",
            ),
            (
                "Acompanhamento",
                "Acompanhamos audiências, prazos e decisões, e você fica sabendo "
                "de cada passo importante.",
            ),
        ],
        "documentos_h2": "O que separar antes de conversar",
        "documentos": [
            "RG e CPF",
            "Certidão de casamento ou documento da união estável",
            "Certidão de nascimento dos filhos",
            "Comprovantes da sua renda e, se souber, da renda da outra parte",
            "Comprovantes dos gastos dos filhos: escola, saúde e alimentação",
            "Documentos dos bens do casal: imóveis, veículos e contas",
            "Acordo ou decisão anterior sobre pensão ou guarda, se houver",
            "Comprovantes dos pagamentos de pensão feitos ou em atraso",
        ],
        "faq": [
            (
                "Preciso esperar o divórcio para pedir pensão?",
                "Não. A pensão dos filhos pode ser pedida a qualquer momento, "
                "antes, durante ou depois do divórcio. O juiz pode fixar um valor "
                "provisório já no início do processo.",
            ),
            (
                "Dá para se divorciar se a outra pessoa não quiser?",
                "Sim. Ninguém é obrigado a continuar casado. Sem acordo, o divórcio "
                "é pedido na Justiça, e bens, guarda e pensão são decididos no "
                "processo.",
            ),
            (
                "Quem pode adotar?",
                "Pessoas maiores de 18 anos, casadas ou não, com pelo menos 16 anos "
                "a mais que a criança. É preciso passar pela habilitação na Vara da "
                "Infância, que é o cadastro de quem quer adotar.",
            ),
            (
                "Moro em outra cidade. Vocês podem me atender?",
                "Sim. Conversamos com você a distância e, quando o processo é "
                "eletrônico, atuamos em qualquer lugar do Brasil. Se algum ato "
                "exigir presença, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato descreve o que está incluído, como o divórcio, a partilha "
                "dos bens ou a pensão.",
            ),
        ],
        "final_h2": "Conte o que está acontecendo na sua família",
    },
    # 4. CÍVEL ---------------------------------------------------------------
    {
        "slug": "civel",
        "nome": "Direito Cível",
        "curto": "Cível",
        "gatilho": "Fui processado ou quero processar",
        "card": (
            "Defesa em processos e ações do dia a dia: cobrança, indenização, "
            "contratos, consumidor e despejo."
        ),
        "seo_titulo": "Advogado cível em Uberlândia | Ferreira e Dutra",
        "seo_descricao": (
            "Defesa em processos cíveis e ações de cobrança, indenização, "
            "contratos, direito do consumidor e despejo em Uberlândia. Fale com o "
            "escritório."
        ),
        "hero_h1": "Foi processado? A defesa tem prazo",
        "hero_p": (
            "Se chegou uma citação, que é o aviso oficial de um processo contra "
            "você, o prazo para se defender começa a contar. Também entramos com "
            "ações de cobrança, indenização, contratos, consumidor e despejo."
        ),
        "cta": "Falar sobre o meu caso",
        "msg": "Olá, preciso de ajuda com um processo.",
        "situacoes_h2": "Problemas do dia a dia que viram processo",
        "situacoes": [
            (
                "Chegou um processo contra mim",
                "Lemos a ação, reunimos as provas e apresentamos a defesa dentro "
                "do prazo. Quanto antes você nos procurar, mais tempo há para "
                "preparar a resposta.",
            ),
            (
                "Tenho dinheiro a receber",
                "Quando alguém deve e não paga, entramos com a cobrança. Se você "
                "tem cheque, nota promissória ou contrato assinado, pode caber a "
                "execução, um caminho mais direto para cobrar.",
            ),
            (
                "Sofri um prejuízo e quero reparação",
                "Avaliamos se houve dano material ou moral e quem é o responsável, "
                "e entramos com o pedido de indenização na Justiça.",
            ),
            (
                "O contrato não foi cumprido",
                "Analisamos o contrato e as conversas entre as partes e pedimos o "
                "cumprimento, o fim do contrato ou a reparação do prejuízo.",
            ),
            (
                "Tive problema com uma empresa",
                "Produto com defeito, cobrança indevida, nome negativado sem motivo "
                "ou serviço não prestado. Atuamos com base no Código de Defesa do "
                "Consumidor.",
            ),
            (
                "O inquilino não paga o aluguel",
                "Entramos com a ação de despejo e a cobrança dos aluguéis "
                "atrasados. Se você é o inquilino e recebeu uma ação de despejo, "
                "fazemos a sua defesa.",
            ),
        ],
        "atuacao_h2": "Como conduzimos o seu processo",
        "atuacao": [
            (
                "Primeiro contato",
                "Você conta o que aconteceu e envia o que tiver: contrato, "
                "mensagens ou a citação. Verificamos logo se há prazo correndo.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar.",
            ),
            (
                "Defesa ou ação",
                "Estudamos os documentos e a lei aplicável e escrevemos a defesa ou "
                "a ação para o seu caso, com as provas organizadas.",
            ),
            (
                "Acompanhamento",
                "Acompanhamos audiências, prazos, tentativas de acordo e recursos, "
                "e você é informado de cada decisão importante.",
            ),
        ],
        "documentos_h2": "O que separar para a primeira conversa",
        "documentos": [
            "RG e CPF, ou os documentos da empresa, se for o caso",
            "A citação ou intimação que você recebeu, se houver",
            "Contratos, recibos, notas fiscais e comprovantes de pagamento",
            "Conversas de WhatsApp, e-mails e notificações sobre o problema",
            "Fotos, laudos ou orçamentos que mostrem o prejuízo",
            "Contrato de aluguel, nos casos de despejo",
            "Nome e dados da outra parte, se você tiver",
        ],
        "faq": [
            (
                "Qual o prazo para me defender?",
                "Na Justiça comum, em regra, são 15 dias úteis, contados conforme a "
                "forma da citação. No Juizado Especial, a defesa costuma ser "
                "apresentada até a audiência. Por isso, procure o escritório assim "
                "que receber a citação.",
            ),
            (
                "O que acontece se eu não responder?",
                "O processo segue sem a sua versão, e o juiz pode considerar "
                "verdadeiros os fatos contados pela outra parte. É o que se chama "
                "de revelia.",
            ),
            (
                "Preciso de advogado no Juizado Especial?",
                "Em causas de até 20 salários mínimos, a lei não exige advogado no "
                "Juizado Especial Cível. Ainda assim, a defesa técnica ajuda a não "
                "perder prazos nem provas.",
            ),
            (
                "O processo é em outra cidade. Vocês podem atuar?",
                "Sim. Quando o processo é eletrônico, atuamos em qualquer lugar do "
                "Brasil e conversamos com você a distância. Se algum ato exigir "
                "presença, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato descreve o que está incluído, como a defesa, as "
                "audiências e eventuais recursos.",
            ),
        ],
        "final_h2": "Conte o que aconteceu e mande o que tiver",
    },
    # 5. TRÂNSITO ------------------------------------------------------------
    {
        "slug": "transito",
        "nome": "Direito de Trânsito",
        "curto": "Trânsito",
        "gatilho": "Minha CNH foi suspensa ou cassada",
        "card": (
            "CNH suspensa ou cassada, recursos de multa, processo no Detran, "
            "acidentes e crimes de trânsito."
        ),
        "seo_titulo": "Advogado de trânsito e CNH em Uberlândia | Ferreira e Dutra",
        "seo_descricao": (
            "Defesa em suspensão e cassação de CNH, recursos de multa, processo no "
            "Detran, acidentes e crimes de trânsito em Uberlândia. Fale com o "
            "escritório."
        ),
        "hero_h1": "CNH suspensa ou cassada: você pode recorrer",
        "hero_p": (
            "O processo no Detran tem prazos curtos para defesa e recurso. "
            "Analisamos a notificação, verificamos se tudo seguiu a lei e "
            "apresentamos a defesa em cada fase."
        ),
        "cta": "Falar sobre a minha CNH",
        "msg": "Olá, preciso de ajuda com a minha CNH.",
        "situacoes_h2": "Da multa ao processo no Detran",
        "situacoes": [
            (
                "Recebi notificação de suspensão da CNH",
                "Apresentamos a defesa no processo do Detran e, se preciso, os "
                "recursos à JARI e ao CETRAN, os órgãos que julgam recursos de "
                "trânsito.",
            ),
            (
                "Minha CNH foi cassada",
                "A cassação é mais grave que a suspensão: só depois de 2 anos é "
                "possível pedir uma nova habilitação. Analisamos o processo e "
                "apresentamos defesa e recursos em cada fase.",
            ),
            (
                "Levei uma multa que considero injusta",
                "Verificamos se a autuação seguiu as regras, como o prazo da "
                "notificação e os dados do auto de infração, e recorremos quando há "
                "fundamento.",
            ),
            (
                "Fui autuado na Lei Seca",
                "A autuação por álcool ou por recusa ao bafômetro gera multa alta e "
                "suspensão da CNH. Fazemos a defesa no Detran e, se houver processo "
                "criminal, também nele.",
            ),
            (
                "Me envolvi em um acidente",
                "Atuamos para cobrar os danos do acidente ou para defender você de "
                "um pedido de indenização, com base no boletim de ocorrência e nas "
                "provas do caso.",
            ),
            (
                "Respondo por crime de trânsito",
                "Lesão ou morte no trânsito, embriaguez ao volante e direção sem "
                "habilitação podem ser crimes. Fazemos a defesa no inquérito e no "
                "processo criminal.",
            ),
        ],
        "atuacao_h2": "Como conduzimos a defesa da sua CNH",
        "atuacao": [
            (
                "Primeiro contato",
                "Você envia a notificação e a CNH. Verificamos o prazo e o que está "
                "em jogo: multa, suspensão ou cassação.",
            ),
            (
                "Proposta e contrato",
                "Explicamos as fases do processo e combinamos os honorários em "
                "contrato escrito, antes de começar.",
            ),
            (
                "Defesa e recursos",
                "Apresentamos a defesa no Detran e, se for preciso, os recursos à "
                "JARI e ao CETRAN, sempre dentro do prazo de cada fase.",
            ),
            (
                "Acompanhamento",
                "Acompanhamos cada decisão e explicamos o que muda para você em "
                "cada fase do processo.",
            ),
        ],
        "documentos_h2": "O que separar antes de falar conosco",
        "documentos": [
            "CNH, foto da frente e do verso",
            "Notificação do Detran ou da autuação",
            "Auto de infração, se você tiver",
            "Extrato de pontos e infrações da CNH, tirado no site ou aplicativo do Detran",
            "Documento do veículo (CRLV)",
            "Boletim de ocorrência, no caso de acidente",
            "Fotos, vídeos ou nomes de testemunhas, se houver",
        ],
        "faq": [
            (
                "Posso dirigir enquanto recorro?",
                "Em regra, sim. A suspensão só passa a valer depois que o processo "
                "no Detran termina, com os recursos julgados. Ainda assim, cada "
                "caso precisa ser conferido na notificação.",
            ),
            (
                "Qual o prazo para recorrer?",
                "O prazo vem escrito na própria notificação e conta a partir do "
                "recebimento. Por isso, procure o escritório assim que ela chegar.",
            ),
            (
                "Recorrer pode piorar a minha situação?",
                "Não. O recurso não aumenta a multa nem os pontos. Se ele for "
                "negado, vale a penalidade que já tinha sido aplicada.",
            ),
            (
                "Minha CNH é de outra cidade. Vocês podem atuar?",
                "Sim. Conversamos com você a distância e, quando o processo é "
                "eletrônico, atuamos em qualquer lugar do Brasil. Se algum ato "
                "exigir presença, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de ver a notificação, apresentamos a proposta por escrito. "
                "O contrato diz quais fases estão incluídas: defesa no Detran, "
                "recurso à JARI e recurso ao CETRAN.",
            ),
        ],
        "final_h2": "Recebeu a notificação? Fale conosco no prazo",
    },
    # 6. ADMINISTRATIVO ------------------------------------------------------
    {
        "slug": "administrativo",
        "nome": "Direito Administrativo",
        "curto": "Administrativo",
        "gatilho": "Sou servidor e respondo a um PAD",
        "card": (
            "Defesa de servidor público em PAD e sindicância e recursos contra "
            "decisões de órgãos públicos."
        ),
        "seo_titulo": "Defesa em PAD e sindicância em Uberlândia | Ferreira e Dutra",
        "seo_descricao": (
            "Defesa de servidor público em PAD e sindicância, recursos "
            "administrativos e processos contra órgãos públicos em Uberlândia. "
            "Fale com o escritório."
        ),
        "hero_h1": "Defesa de servidor em PAD e sindicância",
        "hero_p": (
            "O PAD, processo administrativo disciplinar, apura a conduta de um "
            "servidor e pode terminar em penalidade. Fazemos a defesa desde a "
            "sindicância até os recursos."
        ),
        "cta": "Falar sobre o meu processo",
        "msg": "Olá, preciso de ajuda com um processo administrativo.",
        "situacoes_h2": "Quando o problema é com o poder público",
        "situacoes": [
            (
                "Fui notificado de uma sindicância",
                "A sindicância é a apuração inicial dos fatos. Acompanhamos você "
                "desde essa fase, porque o que é dito nela pode pesar depois no "
                "PAD.",
            ),
            (
                "Abriram um PAD contra mim",
                "Analisamos a acusação, acompanhamos a coleta de provas e "
                "apresentamos a defesa escrita dentro do prazo.",
            ),
            (
                "Fui chamado para depor na comissão",
                "Preparamos você para o interrogatório e acompanhamos o depoimento "
                "diante da comissão, o grupo de servidores que conduz o PAD.",
            ),
            (
                "Recebi uma penalidade",
                "Avaliamos a decisão e apresentamos recurso ou pedido de "
                "reconsideração ao órgão. Se o processo teve falhas, avaliamos "
                "levar o caso à Justiça.",
            ),
            (
                "Um órgão público decidiu contra mim",
                "Multa, licença negada ou direito do servidor recusado. "
                "Apresentamos recurso administrativo e, se necessário, levamos o "
                "caso à Justiça.",
            ),
            (
                "O mesmo fato virou caso criminal",
                "Quando o fato é apurado no PAD e também na área criminal, cuidamos "
                "das duas defesas de forma coordenada, com a mesma linha nos dois "
                "processos.",
            ),
        ],
        "atuacao_h2": "Como conduzimos a sua defesa",
        "atuacao": [
            (
                "Primeiro contato",
                "Você envia a notificação ou a portaria, o documento que abriu o "
                "processo. Verificamos a fase e os prazos que estão correndo.",
            ),
            (
                "Proposta e contrato",
                "Explicamos como vamos atuar e combinamos os honorários em contrato "
                "escrito, antes de começar.",
            ),
            (
                "Estudo e defesa",
                "Lemos o processo inteiro, as provas e os depoimentos e preparamos "
                "a defesa escrita e as perguntas às testemunhas.",
            ),
            (
                "Até a decisão final",
                "Acompanhamos o processo até a decisão e, se houver penalidade, "
                "avaliamos recurso ao órgão ou ação na Justiça.",
            ),
        ],
        "documentos_h2": "O que separar antes de falar conosco",
        "documentos": [
            "Notificação ou portaria que abriu a sindicância ou o PAD",
            "Cópia do processo, se você já tiver acesso",
            "Ficha funcional e documentos do seu cargo",
            "Mensagens, e-mails e documentos ligados aos fatos",
            "Nomes de pessoas que podem servir de testemunha",
            "Decisão ou penalidade recebida, no caso de recurso",
        ],
        "faq": [
            (
                "Preciso de advogado no PAD?",
                "A lei não obriga, mas a defesa técnica ajuda a cumprir prazos, "
                "pedir provas e preparar depoimentos, que seguem regras próprias "
                "em cada estatuto.",
            ),
            (
                "Sindicância e PAD são a mesma coisa?",
                "Não. A sindicância apura os fatos e pode terminar em arquivamento, "
                "em penalidade leve ou na abertura de um PAD. As penalidades mais "
                "graves, como a demissão, exigem PAD. As regras variam conforme o "
                "estatuto de cada órgão.",
            ),
            (
                "A penalidade já foi aplicada. Ainda dá para fazer algo?",
                "Em muitos casos, sim. Dentro do prazo do estatuto, cabe recurso ao "
                "próprio órgão. Se o processo teve falhas, também é possível "
                "questionar a decisão na Justiça.",
            ),
            (
                "Trabalho em outra cidade. Vocês atendem?",
                "Sim. Quando o processo é eletrônico, atuamos em qualquer lugar do "
                "Brasil e conversamos com você a distância. Se algum ato exigir "
                "presença, como um depoimento, avisamos antes de começar.",
            ),
            (
                "Como são combinados os honorários?",
                "Depois de entender o caso, apresentamos a proposta por escrito. O "
                "contrato diz quais fases estão incluídas, como sindicância, PAD, "
                "recurso ou ação judicial.",
            ),
        ],
        "final_h2": "Conte em que fase está o seu processo",
    },
]
