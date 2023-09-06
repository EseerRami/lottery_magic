import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('megaMillions.db',check_same_thread=False)
        self.cursor = self.con.cursor()
        self.create_mega_millions_history_table()
        self.create_games_out_table()
        self.create_settings_table()
        self.create_frequency_table()
        self.create_agreement_table()

    def create_mega_millions_history_table(self):
        """Create history table"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS mega_millions_history(id varchar(50) PRIMARY KEY, draw_date varchar(50), number1 varchar(2) NOT NULL, \
              number2 varchar(2) NOT NULL, number3 varchar(2) NOT NULL,number4 varchar(2) NOT NULL,number5 varchar(2) NOT NULL,mega_ball varchar(2) NOT NULL\
              )")
        self.con.commit()

    def create_games_out_table(self):
        """Create games out table"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS games_out(id integer PRIMARY KEY, number varchar(2), games_out varchar(2))")
        self.con.commit()

    def create_settings_table(self):
        """Create settings table"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS settings(id integer PRIMARY KEY, name varchar(250), email varchar(250))")
        self.con.commit()

    def create_frequency_table(self):
        """Create frequency table"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS frequency(id integer PRIMARY KEY, number varchar(250), frequency varchar(250))")
        self.con.commit()

    def create_agreement_table(self):
        """Create agreement table"""
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS agreement(id integer PRIMARY KEY AUTOINCREMENT, agreement_flag varchar(250), policy_type varchar(250), app_version varchar(250))")
        self.con.commit()

    def create_set(self, id, draw_date, number1, number2, number3, number4, number5, mega_ball):
        """Create a set"""
        self.cursor.execute("INSERT INTO mega_millions_history(id, draw_date, number1,number2,number3,number4,number5,mega_ball) \
           VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (id, draw_date, number1, number2, number3, number4, number5, mega_ball))
        self.con.commit()

    def create_games_out(self, id, number, games_out):
        """Create a games out value"""
        self.cursor.execute("INSERT INTO games_out(id, number, games_out) \
           VALUES(?, ?, ?)", (id, number, games_out))
        self.con.commit()

    def create_frequency(self, id, number, frequency):
        """Create a frequency value"""
        self.cursor.execute("INSERT INTO frequency(id, number, frequency) \
           VALUES(?, ?, ?)", (id, number, frequency))
        self.con.commit()

    def create_agreement(self, agreement_flag, policy_type, app_version):
        """Create an agreement value"""
        self.cursor.execute("INSERT INTO agreement(agreement_flag, policy_type, app_version) \
           VALUES(?, ?, ?)", (agreement_flag, policy_type, app_version))
        self.con.commit()

    def create_settings(self, id, name, email):
        """Create settings"""
        self.cursor.execute("INSERT INTO settings(id, name, email) \
           VALUES(?, ?, ?)", (id, name, email))
        self.con.commit()

    def get_sets(self):
        """Get sets"""
        sets = self.cursor.execute("SELECT * FROM mega_millions_history ORDER BY draw_date DESC").fetchall()

        return sets

    def get_sets_no_id(self):
        """ Get sets but not ID column"""
        sets = self.cursor.execute("SELECT draw_date, number1,number2,number3,number4,number5,mega_ball FROM mega_millions_history ORDER BY draw_date DESC LIMIT 10").fetchall()
        return sets

    def get_max_draw_date(self):
        """ Get max draw date column"""
        sets = self.cursor.execute("SELECT MAX(draw_date) FROM mega_millions_history").fetchone()[0]
        return sets

    def get_agreement(self,policy_type,version,):
        """ Get agreement """
        agreement = self.cursor.execute("SELECT 1 FROM agreement WHERE policy_type = ? AND app_version = ?", (policy_type,version))
        record = agreement.fetchone()
        if record is None:
            record = 0
        return record

    def get_sets_drawn(self, number1, number2, number3, number4, number5, mega_ball):
        """ Validate if a set has ever won """
        sets = self.cursor.execute("SELECT 0 FROM mega_millions_history WHERE number1=? AND number2 = ? AND number3 = ? AND number4 = ? AND number5 = ? AND mega_ball = ? ",(number1,number2,number3,number4,number5,mega_ball))
        record = sets.fetchone()
        if record is None:
            record = 0
        else:
            record = 1

        return record

    def get_games_out(self):
        """Get games out"""
        games_out = self.cursor.execute("SELECT * FROM games_out ORDER BY id DESC").fetchall()
        #completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()

        return games_out
    
    def get_games_out_val(self,val):
        """ Get the value of games out for specific ID """
        #print(val)
        games_out_val = self.cursor.execute("SELECT games_out FROM games_out WHERE id = ? ", (val,)).fetchone()[0]

        return games_out_val

    def get_frequency(self):
        """Get frequency"""
        frequency = self.cursor.execute("SELECT * FROM frequency ORDER BY id DESC").fetchall()
        #completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()

        return frequency

    def get_frequency_avg(self):
        """Get frequency average"""
        frequency = self.cursor.execute("SELECT AVG(frequency) FROM frequency").fetchone()[0]
        #completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()

        return frequency

    def get_frequency_val(self,val):
        """ Get the value of frequency for specific ID """
        #print(val)
        freq_val = self.cursor.execute("SELECT games_out FROM games_out WHERE id = ? ", (val,)).fetchone()[0]

        return freq_val

    def get_settings(self,val):
        """ Get all settings ID """
        #print(val)
        settings = self.cursor.execute("SELECT * FROM settings WHERE id = ? ", (val,)).fetchall()

        return settings

    def get_settings_val(self,val):
        """ Get the value of settings for specific ID """
        #print(val)
        settings = self.cursor.execute("SELECT name, email FROM settings WHERE id = ? ", (val,))
        record = settings.fetchone()
        if record is None:
            record = 0
        return record

    def update_games_out(self, id, games_out):
        """Update Games out table"""
        self.cursor.execute("UPDATE games_out SET games_out = ? WHERE id = ?", (games_out, id)).fetchall()
        #completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()
        self.con.commit()

    def update_frequency(self, id, frequency):
        """Update Frequency table"""
        self.cursor.execute("UPDATE frequency SET frequency = ? WHERE id = ?", (frequency, id)).fetchall()
        #completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()
        self.con.commit()

    def update_settings(self, id, name, email):
        """Update Games out table"""
        #print(name,email,id,sep=";")
        self.cursor.execute("UPDATE settings SET name = ? , email = ? WHERE id = ?", (name, email, id)).fetchall()
        #completed_tasks = self.cursor.execute("SELECT id, task, due_date FROM tasks WHERE completed = 1").fetchall()
        self.con.commit()


    def close_db_connection(self):
        self.con.close()
