CREATE (library: class {name: "Library"}),
(book: class {name: "Books"}),
(reader: class {name: "Readers"}), 

(lib1: node {name: "National Library", country: "Belarus", city: "Minsk"}),

(library)<-[:is {name: "is"}]-(lib1),

(lib1)-[:has {name: "has"}]-> (book),
(lib1)-[:has {name: "has"}]-> (reader),

(r1: node {code: "098622", name: "Platonov Alexander Vladimirovich", address: "Timoshenko street, 14", telephone: "(29)1318218"}),
(r2: node {code: "098623", name: "Sviridova Maria Olegovna", address: "Rokossovsky avenue, 123", telephone: "(25)1314211"}),
(r3: node {code: "097422", name: "Voyshnis Maya Alexsandrovna", address: "Olshevsky street, 35", telephone: "(29)8976248"}),
(r4: node {code: "090923", name: "Moxammadi Ariana", address: "Burdeynaya street, 134", telephone: "(33)6789432"}),
(r5: node {code: "092222", name: "Davidovskaya Yana Sergeevna", address: "Krupskoy street, 15", telephone: "(33)5318086"}),


(reader)<-[:is {name: "is"}]-(r1),
(reader)<-[:is {name: "is"}]-(r2),
(reader)<-[:is {name: "is"}]-(r3),
(reader)<-[:is {name: "is"}]-(r4),
(reader)<-[:is {name: "is"}]-(r5),



(b1: node {code: "011222", name: "To Kill a Mockingbird", author: "Harper Lee", year: 2009}),
(b2: node {code: "675321", name: "Pride and Prejudice", author: "Jane Austen", year: 2015}),
(b3: node {code: "015622", name: "The Great Gatsby", author: "F. Scott Fitzgerald", year: 2007}),
(b4: node {code: "679821", name: "Little Women", author: "Louisa May Alcott", year: 2016}),
(b5: node {code: "679821", name: "Harry Potter and the Philosopher's Stone", author: "J. K. Rowling", year: 2016}),


(book)<-[:is {name: "is"}]-(b1),
(book)<-[:is {name: "is"}]-(b2),
(book)<-[:is {name: "is"}]-(b3),
(book)<-[:is {name: "is"}]-(b4),
(book)<-[:is {name: "is"}]-(b5),


(b1)<-[:borrow {name: "borrow"}]-(r1),
(b2)<-[:borrow {name: "borrow"}]-(r2),
(b3)<-[:borrow {name: "borrow"}]-(r2),
(b2)<-[:borrow {name: "borrow"}]-(r3),
(b4)<-[:borrow {name: "borrow"}]-(r4)