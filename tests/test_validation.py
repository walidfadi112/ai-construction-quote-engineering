from quote_engine.pipeline import run_pipeline

def valid_payload():
    return {'quote_number':'DEV-2026-041','date':'2026-10-06','company':'BatiPro SARL','project':'Rénovation Clermont','items':[{'description':'Isolation','quantity':100,'unit':'m2','unit_price_ht':42,'total_ht':4200}], 'total_ht':4200,'vat_rate':20,'total_ttc':5040,'confidence':0.96}

def test_valid_quote_auto_approved():
    out=run_pipeline(valid_payload())
    assert out['decision']['status']=='AUTO_APPROVED'

def test_inconsistent_ttc_goes_human_review():
    p=valid_payload(); p['total_ttc']=5300
    out=run_pipeline(p)
    assert out['decision']['status']=='HUMAN_REVIEW'
    assert out['decision']['checks']['ttc'] is False
