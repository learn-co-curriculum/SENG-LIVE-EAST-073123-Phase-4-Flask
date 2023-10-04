# Learning Goal

-  Use Flask-SQLAlchemy to join models with many-to-many relationship between models.
-  Review relationships, Primary keys, and Foreign keys
-  Review back_populates property

- productions -< roles >- actors
    - Productions have many roles, and roles belong to productions.
    - Actors have many roles, and roles belong to actors.
    - Roles serve as an intermediary table connecting productions and actors.

# One-to-Many Relationships:
    - Author and Books: One author can write many books, but each book is typically written by one author.
    - Teacher and Students: A teacher can have multiple students in a class, but each student has only one teacher.
    - Parent and Children: A parent can have multiple children, but each child has only two biological parents.
    - Country and Cities: A country can have many cities within its borders, but each city belongs to only one country.
    - Company and Employees: A company can employ many people, but each employee works for one company.
    - Artist and Artworks: An artist can create multiple artworks, but each artwork is typically created by one artist.
    - Doctor and Patients: A doctor can have multiple patients, but each patient has one primary doctor.
    - Playlist and Songs: A playlist can contain many songs, but each song can belong to multiple playlists.
    - Movie Director and Movies: A director can direct several movies, but each movie typically has one director.
    - Website and Web Pages: A website can have multiple web pages, but each web page belongs to one website.

# Many-to-Many Relationships:

    - Students and Courses: Students can enroll in multiple courses, and courses can have multiple students.
    - Actors and Movies: Actors can appear in multiple movies, and movies can feature multiple actors.
    - Tags and Posts: Posts can have multiple tags, and tags can be associated with multiple posts.
    - Customers and Products: Customers can purchase multiple products, and products can be bought by multiple customers.
    - Authors and Genres: Authors can write books in multiple genres, and each genre can have multiple authors.
    - Employees and Projects: Employees can work on multiple projects, and projects can involve multiple employees.
   - Musicians and Bands: Musicians can be part of multiple bands, and bands can have multiple musicians.
    - Teachers and Subjects: Teachers can teach multiple subjects, and subjects can be taught by multiple teachers.
    - Restaurants and Menu Items: Restaurants can offer multiple menu items, and menu items can be found in multiple restaurants.
    - Actors and Awards: Actors can win multiple awards, and awards can be received by multiple actors.