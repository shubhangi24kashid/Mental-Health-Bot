
from transformers import pipeline

def moderate():
    print("Definition:\nDisruptive eating patterns leading to physical and mental health issues.\nIncludes conditions like anorexia nervosa, bulimia nervosa, and binge-eating disorder.\n\nSymptoms:\nAnorexia Nervosa: Extreme calorie restriction, fear of gaining weight.\nBulimia Nervosa: Binge-eating followed by purging behaviors.\nBinge-Eating Disorder: Consuming large amounts of food rapidly, loss of control.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT).\nNutritional Counseling: Guidance on healthy eating habits.\nMedical Monitoring: Especially for severe cases requiring hospitalization.\n\nSelf-Help at Different Levels:\nMild Eating Disorder: Maintain regular, balanced meals.\nModerate Eating Disorder: Establish a support network, consider self-help resources.\nSevere Eating Disorder: Seek professional help immediately, involve family or friends.\n\nWeekend Activities for Relief:\nRelaxation activities like reading or listening to music.\nEngage in non-food-related social events.\nOutdoor activities promoting a positive body-mind connection.\n\nDiet Recommendations:\nWork with a nutritionist for a balanced, sustainable meal plan.\nEmphasize a variety of food groups.\nAvoid extreme diets and restrictive eating habits.\n\nConclusion:\nAddressing eating disorders requires a comprehensive approach involving therapy, nutritional support, and medical monitoring. Early intervention is crucial, and individuals should seek professional help to develop a personalized treatment plan.")
    question_answering = pipeline("question-answering")
    context = ""
    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return


def dangerous():
    print("Definition:\nDisruptive eating patterns leading to physical and mental health issues.\nIncludes conditions like anorexia nervosa, bulimia nervosa, and binge-eating disorder.\n\nSymptoms:\nAnorexia Nervosa: Extreme calorie restriction, fear of gaining weight.\nBulimia Nervosa: Binge-eating followed by purging behaviors.\nBinge-Eating Disorder: Consuming large amounts of food rapidly, loss of control.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT).\nNutritional Counseling: Guidance on healthy eating habits.\nMedical Monitoring: Especially for severe cases requiring hospitalization.\n\nSelf-Help at Different Levels:\nMild Eating Disorder: Maintain regular, balanced meals.\nModerate Eating Disorder: Establish a support network, consider self-help resources.\nSevere Eating Disorder: Seek professional help immediately, involve family or friends.\n\nWeekend Activities for Relief:\nRelaxation activities like reading or listening to music.\nEngage in non-food-related social events.\nOutdoor activities promoting a positive body-mind connection.\n\nDiet Recommendations:\nWork with a nutritionist for a balanced, sustainable meal plan.\nEmphasize a variety of food groups.\nAvoid extreme diets and restrictive eating habits.\n\nConclusion:\nAddressing eating disorders requires a comprehensive approach involving therapy, nutritional support, and medical monitoring. Early intervention is crucial, and individuals should seek professional help to develop a personalized treatment plan.")


    question_answering = pipeline("question-answering")
    context = "" 
    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return


