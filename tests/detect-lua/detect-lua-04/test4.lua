function init (args)
    local needs = {}
    needs["http.request_headers"] = tostring(true)
    needs["flowint"] = {"cnt"}
    return needs
    end

function match(args)
    print "inspecting"
    a = ScFlowintGet(0)
    if a then
        ScFlowintSet(0, a + 1)
    else
        ScFlowintSet(0, 1)
    end

    a = ScFlowintGet(0)
    if a == 2 then
        print "match"
        return 1
    end
    return 0
end
return 0