import redis
from test import rTestDatabase


r=redis.Redis(
    host='localhost',
    decode_responses=True # decode all to utf-8
)

# WARNING!! this will delete all your data
# r.flushdb()

db=rTestDatabase(r)


print(db.country.save(id="ABW", description="Aruba"))
print(db.country.save(id="AFG", description="Afghanistan"))
print(db.country.save(id="AGO", description="Angola"))
print(db.country.save(id="AIA", description="Anguilla"))
print(db.country.save(id="ALA", description="Aland Islands"))
print(db.country.save(id="ALB", description="Albania"))
print(db.country.save(id="AND", description="Andorra"))
print(db.country.save(id="ARE", description="United Arab Emirates"))
print(db.country.save(id="ARG", description="Argentina"))
print(db.country.save(id="ARM", description="Armenia"))
print(db.country.save(id="ASM", description="American Samoa"))
print(db.country.save(id="ATA", description="Antarctica"))
print(db.country.save(id="ATF", description="French Southern Territories"))
print(db.country.save(id="ATG", description="Antigua and Barbuda"))
print(db.country.save(id="AUS", description="Australia"))
print(db.country.save(id="AUT", description="Austria"))
print(db.country.save(id="AZE", description="Azerbaijan"))
print(db.country.save(id="BDI", description="Burundi"))
print(db.country.save(id="BEL", description="Belgium"))
print(db.country.save(id="BEN", description="Benin"))
print(db.country.save(id="BES", description="Bonaire, Sint Eustatius and Saba"))
print(db.country.save(id="BFA", description="Burkina Faso"))
print(db.country.save(id="BGD", description="Bangladesh"))
print(db.country.save(id="BGR", description="Bulgaria"))
print(db.country.save(id="BHR", description="Bahrain"))
print(db.country.save(id="BHS", description="Bahamas"))
print(db.country.save(id="BIH", description="Bosnia and Herzegovina"))
print(db.country.save(id="BLM", description="Saint Barthélemy"))
print(db.country.save(id="BLR", description="Belarus"))
print(db.country.save(id="BLZ", description="Belize"))
print(db.country.save(id="BMU", description="Bermuda"))
print(db.country.save(id="BOL", description="Bolivia, Plurinational State of"))
print(db.country.save(id="BRA", description="Brazil"))
print(db.country.save(id="BRB", description="Barbados"))
print(db.country.save(id="BRN", description="Brunei Darussalam"))
print(db.country.save(id="BTN", description="Bhutan"))
print(db.country.save(id="BVT", description="Bouvet Island"))
print(db.country.save(id="BWA", description="Botswana"))
print(db.country.save(id="CAF", description="Central African Republic"))
print(db.country.save(id="CAN", description="Canada"))
print(db.country.save(id="CCK", description="Cocos (Keeling) Islands"))
print(db.country.save(id="CHE", description="Switzerland"))
print(db.country.save(id="CHL", description="Chile"))
print(db.country.save(id="CHN", description="China"))
print(db.country.save(id="CIV", description="Cote d Ivoire"))
print(db.country.save(id="CMR", description="Cameroon"))
print(db.country.save(id="COD", description="Congo, the Democratic Republic of the"))
print(db.country.save(id="COG", description="Congo"))
print(db.country.save(id="COK", description="Cook Islands"))
print(db.country.save(id="COL", description="Colombia"))
print(db.country.save(id="COM", description="Comoros"))
print(db.country.save(id="CPV", description="Cabo Verde"))
print(db.country.save(id="CRI", description="Costa Rica"))
print(db.country.save(id="CUB", description="Cuba"))
print(db.country.save(id="CUW", description="Curaçao"))
print(db.country.save(id="CXR", description="Christmas Island"))
print(db.country.save(id="CYM", description="Cayman Islands"))
print(db.country.save(id="CYP", description="Cyprus"))
print(db.country.save(id="CZE", description="Czechia"))
print(db.country.save(id="DEU", description="Germany"))
print(db.country.save(id="DJI", description="Djibouti"))
print(db.country.save(id="DMA", description="Dominica"))
print(db.country.save(id="DNK", description="Denmark"))
print(db.country.save(id="DOM", description="Dominican Republic"))
print(db.country.save(id="DZA", description="Algeria"))
print(db.country.save(id="ECU", description="Ecuador"))
print(db.country.save(id="EGY", description="Egypt"))
print(db.country.save(id="ERI", description="Eritrea"))
print(db.country.save(id="ESH", description="Western Sahara"))
print(db.country.save(id="ESP", description="Spain"))
print(db.country.save(id="EST", description="Estonia"))
print(db.country.save(id="ETH", description="Ethiopia"))
print(db.country.save(id="FIN", description="Finland"))
print(db.country.save(id="FJI", description="Fiji"))
print(db.country.save(id="FLK", description="Falkland Islands (Malvinas)"))
print(db.country.save(id="FRA", description="France"))
print(db.country.save(id="FRO", description="Faroe Islands"))
print(db.country.save(id="FSM", description="Micronesia, Federated States of"))
print(db.country.save(id="GAB", description="Gabon"))
print(db.country.save(id="GBR", description="United Kingdom"))
print(db.country.save(id="GEO", description="Georgia"))
print(db.country.save(id="GGY", description="Guernsey"))
print(db.country.save(id="GHA", description="Ghana"))
print(db.country.save(id="GIB", description="Gibraltar"))
print(db.country.save(id="GIN", description="Guinea"))
print(db.country.save(id="GLP", description="Guadeloupe"))
print(db.country.save(id="GMB", description="Gambia"))
print(db.country.save(id="GNB", description="Guinea-Bissau"))
print(db.country.save(id="GNQ", description="Equatorial Guinea"))
print(db.country.save(id="GRC", description="Greece"))
print(db.country.save(id="GRD", description="Grenada"))
print(db.country.save(id="GRL", description="Greenland"))
print(db.country.save(id="GTM", description="Guatemala"))
print(db.country.save(id="GUF", description="French Guiana"))
print(db.country.save(id="GUM", description="Guam"))
print(db.country.save(id="GUY", description="Guyana"))
print(db.country.save(id="HKG", description="Hong Kong"))
print(db.country.save(id="HMD", description="Heard Island and McDonald Islands"))
print(db.country.save(id="HND", description="Honduras"))
print(db.country.save(id="HRV", description="Croatia"))
print(db.country.save(id="HTI", description="Haiti"))
print(db.country.save(id="HUN", description="Hungary"))
print(db.country.save(id="IDN", description="Indonesia"))
print(db.country.save(id="IMN", description="Isle of Man"))
print(db.country.save(id="IND", description="India"))
print(db.country.save(id="IOT", description="British Indian Ocean Territory"))
print(db.country.save(id="IRL", description="Ireland"))
print(db.country.save(id="IRN", description="Iran, Islamic Republic of"))
print(db.country.save(id="IRQ", description="Iraq"))
print(db.country.save(id="ISL", description="Iceland"))
print(db.country.save(id="ISR", description="Israel"))
print(db.country.save(id="ITA", description="Italy"))
print(db.country.save(id="JAM", description="Jamaica"))
print(db.country.save(id="JEY", description="Jersey"))
print(db.country.save(id="JOR", description="Jordan"))
print(db.country.save(id="JPN", description="Japan"))
print(db.country.save(id="KAZ", description="Kazakhstan"))
print(db.country.save(id="KEN", description="Kenya"))
print(db.country.save(id="KGZ", description="Kyrgyzstan"))
print(db.country.save(id="KHM", description="Cambodia"))
print(db.country.save(id="KIR", description="Kiribati"))
print(db.country.save(id="KNA", description="Saint Kitts and Nevis"))
print(db.country.save(id="KOR", description="Korea, Republic of"))
print(db.country.save(id="KWT", description="Kuwait"))
print(db.country.save(id="LAO", description="Lao People s Democratic Republic"))
print(db.country.save(id="LBN", description="Lebanon"))
print(db.country.save(id="LBR", description="Liberia"))
print(db.country.save(id="LBY", description="Libya"))
print(db.country.save(id="LCA", description="Saint Lucia"))
print(db.country.save(id="LIE", description="Liechtenstein"))
print(db.country.save(id="LKA", description="Sri Lanka"))
print(db.country.save(id="LSO", description="Lesotho"))
print(db.country.save(id="LTU", description="Lithuania"))
print(db.country.save(id="LUX", description="Luxembourg"))
print(db.country.save(id="LVA", description="Latvia"))
print(db.country.save(id="MAC", description="Macao"))
print(db.country.save(id="MAF", description="Saint Martin (French part)"))
print(db.country.save(id="MAR", description="Morocco"))
print(db.country.save(id="MCO", description="Monaco"))
print(db.country.save(id="MDA", description="Moldova, Republic of"))
print(db.country.save(id="MDG", description="Madagascar"))
print(db.country.save(id="MDV", description="Maldives"))
print(db.country.save(id="MEX", description="Mexico"))
print(db.country.save(id="MHL", description="Marshall Islands"))
print(db.country.save(id="MKD", description="Macedonia, the former Yugoslav Republic of"))
print(db.country.save(id="MLI", description="Mali"))
print(db.country.save(id="MLT", description="Malta"))
print(db.country.save(id="MMR", description="Myanmar"))
print(db.country.save(id="MNE", description="Montenegro"))
print(db.country.save(id="MNG", description="Mongolia"))
print(db.country.save(id="MNP", description="Northern Mariana Islands"))
print(db.country.save(id="MOZ", description="Mozambique"))
print(db.country.save(id="MRT", description="Mauritania"))
print(db.country.save(id="MSR", description="Montserrat"))
print(db.country.save(id="MTQ", description="Martinique"))
print(db.country.save(id="MUS", description="Mauritius"))
print(db.country.save(id="MWI", description="Malawi"))
print(db.country.save(id="MYS", description="Malaysia"))
print(db.country.save(id="MYT", description="Mayotte"))
print(db.country.save(id="NAM", description="Namibia"))
print(db.country.save(id="NCL", description="New Caledonia"))
print(db.country.save(id="NER", description="Niger"))
print(db.country.save(id="NFK", description="Norfolk Island"))
print(db.country.save(id="NGA", description="Nigeria"))
print(db.country.save(id="NIC", description="Nicaragua"))
print(db.country.save(id="NIU", description="Niue"))
print(db.country.save(id="NLD", description="Netherlands"))
print(db.country.save(id="NOR", description="Norway"))
print(db.country.save(id="NPL", description="Nepal"))
print(db.country.save(id="NRU", description="Nauru"))
print(db.country.save(id="NZL", description="New Zealand"))
print(db.country.save(id="OMN", description="Oman"))
print(db.country.save(id="PAK", description="Pakistan"))
print(db.country.save(id="PAN", description="Panama"))
print(db.country.save(id="PCN", description="Pitcairn"))
print(db.country.save(id="PER", description="Peru"))
print(db.country.save(id="PHL", description="Philippines"))
print(db.country.save(id="PLW", description="Palau"))
print(db.country.save(id="PNG", description="Papua New Guinea"))
print(db.country.save(id="POL", description="Poland"))
print(db.country.save(id="PRI", description="Puerto Rico"))
print(db.country.save(id="PRK", description="Korea, Democratic People\'s Republic of"))
print(db.country.save(id="PRT", description="Portugal"))
print(db.country.save(id="PRY", description="Paraguay"))
print(db.country.save(id="PSE", description="Palestine, State of"))
print(db.country.save(id="PYF", description="French Polynesia"))
print(db.country.save(id="QAT", description="Qatar"))
print(db.country.save(id="REU", description="Réunion"))
print(db.country.save(id="ROU", description="Romania"))
print(db.country.save(id="RUS", description="Russian Federation"))
print(db.country.save(id="RWA", description="Rwanda"))
print(db.country.save(id="SAU", description="Saudi Arabia"))
print(db.country.save(id="SDN", description="Sudan"))
print(db.country.save(id="SEN", description="Senegal"))
print(db.country.save(id="SGP", description="Singapore"))
print(db.country.save(id="SGS", description="South Georgia and the South Sandwich Islands"))
print(db.country.save(id="SHN", description="Saint Helena, Ascension and Tristan da Cunha"))
print(db.country.save(id="SJM", description="Svalbard and Jan Mayen"))
print(db.country.save(id="SLB", description="Solomon Islands"))
print(db.country.save(id="SLE", description="Sierra Leone"))
print(db.country.save(id="SLV", description="El Salvador"))
print(db.country.save(id="SMR", description="San Marino"))
print(db.country.save(id="SOM", description="Somalia"))
print(db.country.save(id="SPM", description="Saint Pierre and Miquelon"))
print(db.country.save(id="SRB", description="Serbia"))
print(db.country.save(id="SSD", description="South Sudan"))
print(db.country.save(id="STP", description="Sao Tome and Principe"))
print(db.country.save(id="SUR", description="Suriname"))
print(db.country.save(id="SVK", description="Slovakia"))
print(db.country.save(id="SVN", description="Slovenia"))
print(db.country.save(id="SWE", description="Sweden"))
print(db.country.save(id="SWZ", description="Swaziland"))
print(db.country.save(id="SXM", description="Sint Maarten (Dutch part)"))
print(db.country.save(id="SYC", description="Seychelles"))
print(db.country.save(id="SYR", description="Syrian Arab Republic"))
print(db.country.save(id="TCA", description="Turks and Caicos Islands"))
print(db.country.save(id="TCD", description="Chad"))
print(db.country.save(id="TGO", description="Togo"))
print(db.country.save(id="THA", description="Thailand"))
print(db.country.save(id="TJK", description="Tajikistan"))
print(db.country.save(id="TKL", description="Tokelau"))
print(db.country.save(id="TKM", description="Turkmenistan"))
print(db.country.save(id="TLS", description="Timor-Leste"))
print(db.country.save(id="TON", description="Tonga"))
print(db.country.save(id="TTO", description="Trinidad and Tobago"))
print(db.country.save(id="TUN", description="Tunisia"))
print(db.country.save(id="TUR", description="Turkey"))
print(db.country.save(id="TUV", description="Tuvalu"))
print(db.country.save(id="TWN", description="Taiwan, Province of China"))
print(db.country.save(id="TZA", description="Tanzania, United Republic of"))
print(db.country.save(id="UGA", description="Uganda"))
print(db.country.save(id="UKR", description="Ukraine"))
print(db.country.save(id="UMI", description="United States Minor Outlying Islands"))
print(db.country.save(id="URY", description="Uruguay"))
print(db.country.save(id="USA", description="United States of America"))
print(db.country.save(id="UZB", description="Uzbekistan"))
print(db.country.save(id="VAT", description="Holy See (Vatican City State)"))
print(db.country.save(id="VCT", description="Saint Vincent and the Grenadines"))
print(db.country.save(id="VEN", description="Venezuela, Bolivarian Republic of"))
print(db.country.save(id="VGB", description="Virgin Islands, British"))
print(db.country.save(id="VIR", description="Virgin Islands, U.S."))
print(db.country.save(id="VNM", description="Viet Nam"))
print(db.country.save(id="VUT", description="Vanuatu"))
print(db.country.save(id="WLF", description="Wallis and Futuna"))
print(db.country.save(id="WSM", description="Samoa"))
print(db.country.save(id="YEM", description="Yemen"))
print(db.country.save(id="ZAF", description="South Africa"))
print(db.country.save(id="ZMB", description="Zambia"))
print(db.country.save(id="ZWE", description="Zimbabwe"))