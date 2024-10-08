# datascript-leparking
Script to download advert price detail from online car marketplace aggregator leparking

Last tested March 2024
HTML targets are likely to change

Ethical Note

Legal framework on Data scraping is subject to specific cases and local law.
The website's terms of use page states that the use of robots, namely spiders, is prohibited unless done with prior authorisation.

Extract:
1. Propriété intellectuelle

L'ensemble des éléments constituant le site Leparking.fr (textes, graphismes, logiciels, photographies, images, vidéos, sons, plans, noms, logos, marques, créations et œuvres protégeables diverses, bases de données, etc...) ainsi que le site lui-même, relèvent des législations françaises et internationales sur le droit d'auteur et sur les droits voisins du droit d'auteur (notamment les articles L122-4 et L122-5. du Code de la Propriété Intellectuelle). Ces éléments sont la propriété exclusive de ADS4ALL, hormis les éléments réalisés par des intervenants extérieurs au site leparking.fr n'ayant pas cédé leurs droits d'auteur. En conséquence, l'utilisateur du site Leparking.fr s'engage à ne pas :
- utiliser ou interroger le site Leparking.fr pour le compte ou au profit d'autrui ;
- reproduire en nombre, à des fins commerciales ou non, des informations ou des petites annonces présentes sur le site Leparking.fr ;
- intégrer tout ou partie du contenu du site Leparking.fr dans un site tiers
à des fins commerciales ou non ;
- utiliser un robot, notamment d'exploration (spider), une application de recherche ou récupération de sites Internet ou tout autre moyen permettant de récupérer ou d'indexer tout ou partie du contenu du site leparking.fr, excepté en cas d'autorisation expresse et préalable de ADS4ALL.
https://www.leparking.fr/mentions.html

As of March 2024 a robot.txt file was not found.
As of the upload of this script, 6 months have passed since authorisation requests where sent to the website owner and parent business with no response.

Further notes
Testing suggests that sending more than 5 URL requests a minute creates a throttled response.
The script has no workaround implemented for downloading the price data, other than automated refusal of cookies.
The script is not aimed at downloading personal information and rather to monitor price movements and trends in the market.

Information on legal:
Key Aspects of the UK’s Position on Data Scraping:

    Data Protection and GDPR: The UK has its own version of the General Data Protection Regulation (UK-GDPR) following Brexit, which governs the processing of personal data. If scraping involves collecting personal data, the organization must ensure compliance with the principles of UK-GDPR, such as having a lawful basis for data collection (e.g., legitimate interest) and adhering to transparency and data minimization requirements. Organizations also need to avoid scraping sensitive categories of personal data unless they meet stringent legal requirements​(CROLT
    )​(Royal Society
    ).

    Intellectual Property Considerations: The UK offers specific protections for databases under the "sui generis" database right. This right protects databases where substantial investment has been made in obtaining, verifying, or presenting the contents. Scraping a protected database without authorization may constitute a breach of this right, even if the data itself is not copyrighted. This distinguishes the UK from other jurisdictions like the US, where similar protections do not exist​(Oxford Law Blogs
    ).

    Contractual and Terms of Service: While scraping may not constitute a criminal offense, violating a website’s terms of service can lead to civil claims, including breach of contract or tortious interference. Courts may grant website owners injunctions against unauthorized scraping activities that breach terms of service, making it essential for scrapers to review and comply with website policies before scraping​(Oxford Law Blogs
    ).

    Text and Data Mining (TDM) Exceptions: The UK has a limited copyright exception for text and data mining (TDM) specifically for non-commercial research purposes. This exception allows some TDM activities without the copyright holder’s permission but is narrowly defined and does not extend to commercial use​(CROLT
    ).

    Regulatory Bodies and Compliance: The Information Commissioner’s Office (ICO) oversees compliance with data protection laws, while other regulatory bodies like the Competition and Markets Authority (CMA) and the Centre for Data Ethics and Innovation (CDEI) provide guidance on issues related to data governance and digital innovation​(Royal Society
    ).

The UK’s stance on data scraping is shaped by its unique regulatory environment, making it important for businesses to carefully navigate the legal considerations associated with scraping activities. For a detailed understanding, consulting with legal professionals or reviewing specific regulations is recommended.


Key Aspects of the EU’s Position on Data Scraping:

    Legal Basis for Scraping: Under GDPR, scraping personal data requires a clear legal basis. Consent is typically not feasible for scraping due to the scale and nature of the activity. Legitimate interest is often cited, but it must balance the interests of the data controller (e.g., the organization scraping data) against the privacy rights of the data subjects. This is a complex evaluation that requires considering the reasonable expectations of individuals and implementing safeguards to protect their privacy​(Privacy Professionals
    ).

    Restrictions and Safeguards: Organizations must ensure that scraping is conducted in a manner that respects data minimization, storage limitation, and transparency principles. The European Data Protection Board (EDPB) has emphasized that any legitimate interest in scraping must be backed by strong safeguards, such as filtering out sensitive data and ensuring compliance with individuals' rights, such as the right to object to processing​(Privacy Professionals
    ).

    Special Permissions and Directives: Certain organizations, like research institutions or cultural heritage organizations, have special permissions under the EU’s Digital Single Market Directive for text and data mining (TDM). This allows them to scrape data for research purposes, provided they have lawful access to it (e.g., public data or licensed access)​(The Markup
    ).

    Terms of Service (ToS) Considerations: In Europe, violating a website’s terms of service (ToS) is not considered a criminal offense, but it can still lead to civil suits for breach of contract or tort. This is similar to the U.S. position post-Van Buren. However, website owners can implement technical measures such as rate limiting or use the Robots Exclusion Protocol to restrict scraping. Legal outcomes depend on whether such restrictions are bypassed​(The Markup
    ).

Overall, data scraping in Europe is highly regulated, and organizations must be cautious to ensure compliance with GDPR and other directives. Legal considerations for scraping involve navigating privacy laws, intellectual property rights, and contractual obligations, making it advisable to consult legal counsel before engaging in large-scale scraping activities.


Key Aspects of the US's Position on Data Scraping:

The current position in the United States on data scraping is a complex and evolving issue, particularly in the context of advancements in AI and privacy concerns.

    Legality of Web Scraping: Web scraping remains legal in the U.S., but it is subject to conditions. Recent court cases have reaffirmed its legality, particularly for scraping publicly available information, which has been crucial for training AI models. However, there is a growing debate over whether scraping without explicit permission from website owners could lead to regulatory changes or new legislative actions, particularly due to privacy concerns related to AI models and the data they consume​(Center for Data Innovation
    ).

    Privacy and Data Protection Concerns: There is significant concern over the lack of comprehensive data protection laws in the U.S. The government and private entities can purchase personal data from third-party data brokers, creating potential risks for individual privacy and misuse. Legislative efforts are ongoing to close these loopholes and ensure that data brokers do not bypass legal protections such as the Fourth Amendment. Proposals have been made to limit the collection and sale of sensitive data, but comprehensive legislation has not yet been passed​(Brennan Center for Justice
    ).

    Legal Developments in Data Breach Cases: U.S. courts have shown mixed stances on data breach lawsuits, especially regarding the standing of plaintiffs to sue for damages based on future harm. The Supreme Court’s ruling in TransUnion v. Ramirez (2021) clarified that the mere risk of future harm is insufficient to confer standing for damages in data breach cases, unless the plaintiff can show that the harm is similar to a traditionally recognized basis for a lawsuit (e.g., reputational harm). This decision has influenced lower courts' rulings, making it harder for plaintiffs to establish standing based on potential future misuse of their data​(Privacy Professionals
    ).

    Industry Self-Regulation and Standards: In response to rising concerns, the private sector has taken some self-regulatory measures. For instance, AI companies have adopted the use of the Robots Exclusion Protocol to allow websites to block their crawlers. Some companies, like Adobe, have introduced the "Do Not Train" metadata standard to prevent AI models from using specific content in their datasets. These industry-led standards aim to reduce the need for regulatory intervention while balancing the needs of website owners and AI developers​(Center for Data Innovation
    ).

Overall, while the legality of data scraping is maintained, privacy concerns and the potential for misuse continue to drive discussions on whether new regulations are necessary. This legal landscape is likely to continue evolving as technology and AI applications advance further.

*The information on legal was researched by this account owner, and the text above provided by ChatGPT AI. 
