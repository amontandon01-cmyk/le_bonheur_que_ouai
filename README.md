# Le Bonheur Qué Ouai

Site statique de Mélanie Vonlanthen : coaching, accompagnement privé, transitions de vie, remise en mouvement et tournages / missions. Huit pages HTML, sans étape de compilation.

## État de publication

GitHub Pages sert de version de validation avant bascule du domaine officiel. Chaque page contient `noindex,follow`. Le sitemap reste vide en préproduction. `robots.txt` autorise la lecture pour permettre aux moteurs de constater `noindex` (le fichier d'un projet GitHub Pages sous un sous-chemin ne contrôle pas les robots à la racine du domaine).

Le choix du domaine et la publication définitive restent à confirmer. Ne pas activer l'indexation de deux copies identiques.

## Améliorations préparées

- Accueil explicite sur le coaching à Neuchâtel et les formats ; titres propres à chaque besoin.
- Typographie plus mesurée, espacements harmonisés, navigation uniforme et liens de contact actifs.
- Contenu et navigation accessibles sans JavaScript, lien d'évitement, focus visible et boucle clavier du menu mobile.
- Fils d'Ariane visibles ; données structurées cohérentes pour les services, la personne, l'entreprise, le contact et la FAQ. Réponses structurées issues des réponses visibles.
- Liens entre pages de situation, formats et FAQ ; explication du premier échange.
- Chargement des polices dans le HTML au lieu d'un `@import` CSS.
- Photographies, logo, coordonnées et éléments du parcours existants conservés. Aucun avis client, diplôme, tarif ou résultat garanti ajouté.

## Préparer l'indexation

Le script suivant actualise ensemble les URL canoniques, `og:url`, les identifiants et liens JSON-LD, les directives d'indexation, le sitemap et sa déclaration. Il ne configure ni le DNS ni le domaine GitHub Pages.

Après confirmation du domaine, de son routage et des contenus :

```sh
python scripts/configure_seo.py --base-url https://www.lebonheurqueouai.ch/ --production
```

Pour conserver / rétablir la préproduction :

```sh
python scripts/configure_seo.py --base-url https://amontandon01-cmyk.github.io/le_bonheur_que_ouai/
```

Avant bascule, confirmer que l'adresse, les formations, les plus de 5’000 heures et les formats annoncés restent exacts. Ces informations proviennent du contenu existant et n'ont pas été vérifiées indépendamment. Prévoir les redirections des anciennes pages et la déclaration du sitemap dans Search Console. Les assets chargés depuis l'ancien domaine doivent rester accessibles ou être rapatriés avant sa fermeture.

## Vérifications effectuées

Huit pages : liens internes, fragments, références d'assets comparées à l'arborescence GitHub, un H1 par page, métadonnées, JSON-LD et huit réponses FAQ. Syntaxe JavaScript vérifiée. Bascule production / préproduction et réexécution identique vérifiées dans une copie temporaire. Pas de test navigateur, de mesure Lighthouse ni de vérification d'indexation réelle ; le rendu visuel reste à valider.

## Références SEO / IA

- https://developers.google.com/search/docs/appearance/ai-features
- https://developers.google.com/search/docs/crawling-indexing/block-indexing

Les contenus utiles, accessibles et cohérents servent aussi les réponses IA. Aucun balisage spécifique ne garantit leur citation ou leur classement.
