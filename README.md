# Le Bonheur Qué Ouai

Site statique de Mélanie Vonlanthen : coaching, accompagnement privé, transitions de vie, remise en mouvement et tournages / missions. Neuf pages HTML, sans étape de compilation.

## État de publication

Le site officiel reste https://www.lebonheurqueouai.ch/. GitHub Pages reste durablement la version de travail publique ; aucune migration n’est prévue à ce stade. Chaque page contient `noindex,follow`. Le sitemap reste vide en préproduction. `robots.txt` autorise la lecture pour permettre aux moteurs de constater `noindex` (le fichier d'un projet GitHub Pages sous un sous-chemin ne contrôle pas les robots à la racine du domaine).

Les changements de cette version sont publiés sur GitHub Pages pour retours. Conserver la non-indexation de cette version de travail. Ne pas relancer la question d’une migration sans demande explicite.

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

## Intégration FIDES (13 septembre 2026)

Page dédiée `methode-fides.html`, accès depuis toutes les navigations, présentation sur l’accueil, liens depuis les formats, le portrait et la FAQ. Orthographe FIDES vérifiée sur le site officiel. La présentation reprend les notions publiques de schémas, libre arbitre et rythme individuel, sans inventer un protocole ni reprendre de promesse de guérison. Les questions de réflexion sont une rédaction éditoriale, pas les étapes officielles de la méthode.

Sources du contenu :
- https://www.lebonheurqueouai.ch/coaching-personnalise
- https://www.lebonheurqueouai.ch/portrait
- https://www.lebonheurqueouai.ch/formation

Le seuil du menu mobile passe à 1’200 px pour accueillir le lien FIDES.

## Portrait et identité visuelle (13 septembre 2026)

Le portrait explicite l’intelligence relationnelle à travers la pratique : écoute du contexte et des émotions, discernement, franchise, ressources et orientation professionnelle. Ces éléments proviennent de l’échange validé avec Mélanie et de son parcours. Aucun diagnostic, score psychométrique ni détail de santé personnel n’est publié. Une synthèse figure dans l’accueil, et la page FIDES relie cette posture à sa démarche.

Identité visuelle : `assets/brand/logo-original.png` est la copie exacte du logo fourni par le site officiel. `logo-symbol.png` utilise sa silhouette alpha sans la redessiner, dans une teinte blanc chaud. Cette même version sert au menu et aux icônes (fond sombre pour l’onglet et les raccourcis mobiles). Les anciens favicons ont été remplacés. Les icônes, le manifeste, le CSS et le JS portent un paramètre de version pour actualiser les caches. Le manifeste reste en affichage navigateur, sans service worker ni promesse de fonctionnement hors connexion.
