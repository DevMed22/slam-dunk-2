from .statsbomb import match_data, matches_id, com_dict, season_dict, get_comp, com_name, season_name
from django.shortcuts import render
d = True
def comps(request):
    if request.method == 'POST':    
        season = request.POST['season']
        comp = request.POST['comp']
        data = get_comp(season, comp)
        print(comp, season)
        return data
    return render(request, 'comps/comps.html', {'comps':com_dict, 'ses':season_dict})

        


def result(request):
    
    if 'match' in request.POST:
        match = request.POST['match']
        h,w,s1,s2,stad,h_m,a_m,c_s = match_data(data,m_idx[m_name[0]])
        print(h,w,s1,s2,stad,h_m,a_m,c_s)
        contex={
            'Home':h,
            'Away':w,
            'HScore':s1,
            'AScore':s2,
            'Stadium':stad,
            'HManager':h_m,
            'AManager':a_m,
            'CStage':c_s,
        }
        return render(request, 'comps/result.html', contex)
    return render(request, 'comps/matches.html', {'matches':m_name})
    
