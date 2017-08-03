
from queue import Queue

class Match(object):
    """Represents game match active"""

    def __init__(self, groups):
        self.match_group_blue = groups[0]
        self.match_group_red = groups[1]
        self.match_max_time_secs = 1800
        self.match_name = "Default"

class Group(object):
    """Stores group of parties"""
    def __init__(self, parties_list):
        super(Group, self).__init__()
        self.parties_list = parties_list


class PlayerParty(object):
    """Stores party of users"""
    def __init__(self, users_group):
        super(PlayerParty, self).__init__()
        self.users_group = users_group
        self.is_ready = True if len(users_group) == 4 else False

    def __str__(self):
        return "|".join([user.selected_class for user in self.users_group])

    def is_user_in_group(self, user_id):
        for user in self.users_group:
            if user_id == user.id:
                return True

        return False

    def get_party_members_len():
        return lent(self.users_group)

class GroupStorageController(object):
    """Class to store all the groups in the game"""

    __parties_list = []
    __waiting_groups_queue = Queue()
    __matches_in_game_list = []

    @classmethod
    def add_new_group(cls, users_group):
        # Search for other groups to craeate a solid group
        # Once search finished add group to waiting group if group is not done
        # else add group to ready groups dict

        new_party = PlayerParty(users_group)
        cls.__parties_list.append(new_party)
        print(new_party)
        if new_party.is_ready:
            new_group = Group([new_party])
            cls.__waiting_groups_queue.put(new_group)
        else:

            cls.__try_create_group()


        cls.__try_start_game()
        cls.__show_parties()

    @classmethod
    def try_delete_group_by_user_id(cls, user_id):
        group = cls.__find_user_group(user_id)



    @classmethod
    def __find_user_group(cls, user_id):
        found_party = next( (party for party in cls.__parties_list if party.is_user_in_group(user_id)), default_value)
        return party


    @classmethod
    def __try_start_game(cls):

        if cls.__waiting_groups_queue.qsize() >= 2:
            ready_group1 =  cls.__waiting_groups_queue.get() if not cls.__waiting_groups_queue.empty() else None
            ready_group2 =  cls.__waiting_groups_queue.get() if not cls.__waiting_groups_queue.empty() else None

            if ready_group1 and ready_group2:
                print("CRETAE MATCH")
                match = Match((ready_group1, ready_group2))
                cls.__matches_in_game_list.append(match)

                cls.__remove_parties(ready_group1.parties_list)
                cls.__remove_parties(ready_group2.parties_list)

    @classmethod
    def __get_parties_by_members_number(cls, memebers_number):
       return [party for party in cls.__parties_list if party.get_party_members_len() == memebers_number]

    @classmethod
    def __remove_parties(cls, parties_list):
        for party in parties_list:
            print("removing " + str(party))
            cls.__parties_list.remove(party)

    @classmethod
    def __show_parties(cls):
        print("--- Witing list ---")
        for party in cls.__parties_list:
            print(party)


    @classmethod
    def __try_create_group(cls):

        new_party_members = new_party.get_party_members_len()
        party_sub_list = cls.__get_parties_by_members_number(3)
        if(len(party_sub_list) )

    @classmethod
    def __try_add_group_of_three(cls):
        pass