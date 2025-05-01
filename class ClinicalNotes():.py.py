# Get variable metadata for context prompt.
        self.var_dict = dict()
        self.alleles = []             # exogenous variables.
        self.family_history = []      # exogenous variables.
        self.previous_surgeries = []  # exogenous variables.
        self.disease = ''.join(choices(string.ascii_uppercase+string.digits, k=6))
        self.pain_threshold = np.random.choice(["7/10", "8/10", "9/10"], size = 1).item()
        self.exog_names = [''.join(choices(string.ascii_uppercase+string.digits, k=4)) for _ in self.nodes]
        endog_options = ["lab", "vital"]
        exog_options = ["carries allele", "has a family history of", "has previously received surgery for"]
        magnitudes = ["elevated", "low"]

        for var,u in zip(self.nodes,self.exog_names):
        
            parents = get_parents(var, self.nodes, adj)
            endog = np.random.choice(endog_options, size = 1).item()
            exog = np.random.choice(exog_options, size = 1).item()
        
            # Store exogenous variables by type.
            if "allele" in exog:
                self.alleles.append(u)
            elif "family" in exog:
                self.family_history.append(u)
            elif "surgery" in exog:
                self.previous_surgeries.append(u)
        
            # Get magnitudes.
            mag = np.random.choice(magnitudes, size = 1).item()
            level = str(round(np.random.uniform(low = 0.1, high = 3.5, size = 1).item(), 2))+" mg/dL"
            if mag == "low":
                level = "less than "+level
            else:
                level = "greater than "+level
                
            self.var_dict[var] = {"parents": parents,
                                  "endog type": endog, 
                                  "endog magnitude": mag, 
                                  "endog level": level,
                                  "exog var name": u, 
                                  "exog type": exog}

        # Get patient sex and name according to sex.
        self.sex = np.random.choice(["male", "female"], size = 1).item()
        f = Faker()
        if self.sex == "female":
            self.name = f.name_female()
        else:
            self.name = f.name_male()
        
        # Get age and pain details.
        self.age = np.random.randint(low = 53, high = 70, size = 1).item()
        self.hours = np.random.randint(low = 2, high = 6, size = 1).item()
        self.rating = str(np.random.randint(low = 4, high = 11, size = 1).item())+"/10"
        self.mg = np.random.choice([75,100,250,500], size = 1).item()
        
        # Get observed alleles.
        if len(self.alleles) > 0:
            total_alleles = np.random.randint(low = 1, high = len(self.alleles)+1, size = 1).item()
        else:
            total_alleles = 0
        self.obs_alleles = list(np.random.choice(self.alleles, size = total_alleles))
        self.extra_alleles = ["".join(choices(string.ascii_uppercase+string.digits, k=4)) for _ in range(n_extra_vars)]
        obs_alleles_str = ", ".join(self.obs_alleles+self.extra_alleles)
        
        # Get observed family medical history.
        if len(self.family_history) > 0:
            total_family_history = np.random.randint(low = 1, high = len(self.family_history)+1, size = 1).item()
        else:
            total_family_history = 0
        self.obs_family_history = list(np.random.choice(self.family_history, size = total_family_history))
        self.extra_family_history = ["".join(choices(string.ascii_uppercase+string.digits, k=4)) for _ in range(n_extra_vars)]
        obs_family_history_str = ", ".join(self.obs_family_history+self.extra_family_history)
        
        # Get observed surgical history.
        if len(self.previous_surgeries) > 0:
            total_previous_surgeries = np.random.randint(low = 1, high = len(self.previous_surgeries)+1, size = 1).item()
        else:
            total_previous_surgeries = 0
        self.obs_previous_surgeries = list(np.random.choice(self.previous_surgeries, size = total_previous_surgeries))
        self.extra_previous_surgeries = ["".join(choices(string.ascii_uppercase+string.digits, k=4)) for _ in range(n_extra_vars)]
        obs_previous_surgeries_str = ", ".join(self.obs_previous_surgeries+self.extra_previous_surgeries)
        
        # Get observed medications (not used in causal graph).
        n_meds = np.random.randint(low = 1, high = 3, size = 1).item()
        medications = ["".join(choices(string.ascii_uppercase+string.digits, k=3)) for _ in range(n_meds)]
        amounts = [str(np.random.choice([10,25,50,75,100,150],size=1).item()) for _ in range(n_meds)]
        self.medications = [x+" "+y+" mg/day" for x,y in zip(medications,amounts)]
        medications = ", ".join(self.medications)
        
        # Get observed exogenous values (binary).
        self.exog_obs = self.obs_family_history + self.obs_alleles + self.obs_previous_surgeries
        self.exog_true_binary = [int(var in self.exog_obs) for var in self.exog_names]

        # Construct prompt.
        intro = "Chronic disease {} sometimes requires surgical intervention, \
        depending on genetics, vital signs, and lab results. The patient will experience \
        significant pain (rated greater than or equal to {}) if they carry allele {}, \
        a genetic marker for severe {}.".format(self.disease,
                                                self.pain_threshold,
                                                self.exog_vars[0],
                                                self.disease)
        outro = "Assume that all factors influencing the surgeon are fully described here."
        strngs = [intro]
        for var,terms in self.var_dict.items():
            if var == "pain":
                continue
            parents = terms.get("parents")
            endog_type = terms.get("endog type")
            magnitude = terms.get("endog magnitude")
            level = terms.get("endog level")
            exog = "the patient "+terms.get("exog type")+" "+terms.get("exog var name")
        
            parent_strngs = []
            for parent in parents:
                if parent == "pain":
                    parent = "the patient self-reports significant pain"
                else:
                    parent_terms = var_dict.get(parent)
                    parent = "{} is {}".format(parent,parent_terms.get("endog magnitude"))
                parent_strngs.append(parent)
            parent_strngs.append(exog)
            if var != leaf:
                if var == root:
                    strng = " and ".join(parent_strngs)
                else:
                    strng = " or ".join(parent_strngs)
                strng = "If " + strng + ", then {} {} will be {} ({}).".format(endog_type,
                                                                               var,
                                                                               magnitude,
                                                                               level)
            else:
                strng = " and ".join(parent_strngs)
                strng = "If " + strng + ", then the surgeon will recommend surgery.".format(endog_type,
                                                                                            var,
                                                                                            magnitude,
                                                                                            level)
            strngs.append(strng)
        strngs.append(outro)
        
        self.context = " ".join(strngs)

        # Add patient history.
        history = "Now, we will review the history and physical notes for patient {}. \
        History of Present Illness: {} is a {}-year-old {} with {} who presented to the \
        emergency department with acute onset pain that began {} hours prior to arrival. The \
        pain was rated {}. The patient reports the pain has been persistent since onset. \
        The patient took aspirin {} mg at home with minimal relief. \
        Genetic Screening: Patient carries alleles {}. \
        Family History: {}. \
        Medications: {}. \
        Past Surgical History: Prior surgeries for {}.".format(self.name,self.name,self.age,self.sex,
                                                               self.disease,self.hours,self.rating,self.mg,
                                                               obs_alleles_str,
                                                               obs_family_history_str,
                                                               medications,
                                                               obs_previous_surgeries_str)
        self.context += history
        return self.context