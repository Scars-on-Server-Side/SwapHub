-- Перед выполнением запустить скрипты:
-- 1. `database/country-region-city.sql`
-- 2. `database/categories.sql`


-- Users
INSERT INTO auth_user
    (id, "password", is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES
    ('2', 'pbkdf2_sha256$600000$5ZgY7DTTq0UE3YxVF1nR8m$R74iqbzG8ZxglapkW69+cjlCfbx5Qhq31Ug8BD/2JsM=', 'False', 'dmitriy.popov', 'Дмитрий', 'Попов', 'dmitriypopov@mail.ru', 'False', 'True', NOW()),
    ('3', 'pbkdf2_sha256$600000$5ZgY7DTTq0UE3YxVF1nR8m$R74iqbzG8ZxglapkW69+cjlCfbx5Qhq31Ug8BD/2JsM=', 'False', 'pavel.lomonosov', 'Павел', 'Ломоносов', 'pavellomonosov@mail.ru', 'False', 'True', NOW()),
    ('4', 'pbkdf2_sha256$600000$5ZgY7DTTq0UE3YxVF1nR8m$R74iqbzG8ZxglapkW69+cjlCfbx5Qhq31Ug8BD/2JsM=', 'False', 'aleksandr.morozov', 'Александр', 'Морозов', 'aleksandrmorozov@mail.ru', 'False', 'True', NOW()),
    ('5', 'pbkdf2_sha256$600000$5ZgY7DTTq0UE3YxVF1nR8m$R74iqbzG8ZxglapkW69+cjlCfbx5Qhq31Ug8BD/2JsM=', 'False', 'anna.repina', 'Анна', 'Репина', 'annarepina@yandex.ru', 'False', 'True', NOW()),
    ('6', 'pbkdf2_sha256$600000$5ZgY7DTTq0UE3YxVF1nR8m$R74iqbzG8ZxglapkW69+cjlCfbx5Qhq31Ug8BD/2JsM=', 'False', 'olesya.olegovna', 'Олеся', 'Олеговна', 'olesyaolegovna@gmail.com', 'False', 'True', NOW())


-- Locations
INSERT INTO loc_location 
    (id, city_id, country_id, region_id)
VALUES
    ('1', '1', '0', '0'),
    ('2', '173', '0', '1')


-- User Profiles
INSERT INTO main_userprofile
    (id, location_id, user_id)
VALUES
    ('1', '2', '2'),
    ('2', '2', '3'),
    ('3', '1', '4'),
    ('4', '2', '5'),
    ('5', '1', '6')


-- Thing


-- Trade


-- Feedback